import difflib
import tokenize
from lib2to3.pgen2.parse import ParseError
from pathlib import Path

from unimport.config import Config
from unimport.refactor import RefactorTool
from unimport.scan import Scanner


class Session:
    def __init__(self, config_file=None):
        self.config = Config(config_file)
        self.scanner = Scanner()
        self.refactor_tool = RefactorTool()

    def _read(self, path):
        try:
            with tokenize.open(path) as stream:
                source = stream.read()
                encoding = stream.encoding
        except OSError as exc:
            print(f"{exc} Can't read")
            return "", "utf-8"
        else:
            return source, encoding

    def _list_paths(self, start, pattern):
        start = Path(start)

        def _is_excluded(path):
            for pattern_exclude in self.config.exclude:
                for inner in start.glob(pattern_exclude):
                    if str(path).startswith(str(inner)):
                        return True

        if not start.is_dir():
            if not _is_excluded(start):
                yield start
        else:
            for path in start.glob(pattern):
                if not _is_excluded(path):
                    yield path


    def scan_directory(self, path, recursive=False):
        pattern = "*.py"
        if recursive:
            pattern = f"**/{pattern}"
        for path in self._list_paths(path, pattern):
            yield from self.scan_file(path)

    def refactor(self, source):
        modules = [module["name"] for module in self.get_unused_imports(source)]
        return self.refactor_tool.refactor_string(source, modules)

    def refactor_file(self, path, apply=False):
        path = Path(path)
        source, encoding = self._read(path)
        try:
            result = self.refactor(source)
        except ParseError as exc:
            raise ValueError(f"Invalid python file {path}.") from exc
        if apply:
            path.write_text(result, encoding=encoding)
        else:
            return result

    def diff(self, source):
        result = self.refactor(source)
        return tuple(
            difflib.unified_diff(source.splitlines(), result.splitlines())
        )

    def diff_file(self, path):
        source, _ = self._read(path)
        result = self.refactor_file(path, apply=False)
        return tuple(
            difflib.unified_diff(
                source.splitlines(), result.splitlines(), fromfile=str(path)
            )
        )

    def get_unused_imports(self, source):
        self.scanner.run_visit(source)
        for imp in self.scanner.imports:
            len_dot = len(imp["name"].split("."))
            for name in self.scanner.names:
                if ".".join(name["name"].split(".")[:len_dot]) == imp["name"]:
                    break
            else:
                yield imp
        self.scanner.clear()
