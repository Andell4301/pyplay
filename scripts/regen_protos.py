from logging import getLogger
from pathlib import Path
from subprocess import run

logger = getLogger(__name__)


PYPLAY_DIR = Path(__file__).resolve().parent.parent / "pyplay"
PROTO_SOURCE_DIR = PYPLAY_DIR / "res" / "protos"
PROTO_OUTPUT_DIR = PYPLAY_DIR / "playprotos"


def main(protoc_exe: Path | str) -> None:
    logger.info("Regenerating proto file...")

    PROTO_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (PROTO_OUTPUT_DIR / "__init__.py").touch()

    for proto_path in PROTO_SOURCE_DIR.glob("*.proto"):
        run(
            [
                protoc_exe,
                str(proto_path),
                f"--proto_path={PROTO_SOURCE_DIR}",
                f"--python_out={PROTO_OUTPUT_DIR}",
                f"--pyi_out={PROTO_OUTPUT_DIR}",
            ],
            check=True,
        )
    for f in PROTO_OUTPUT_DIR.iterdir():
        if "_pb2" in f.stem:
            new_name = f.stem.replace("_pb2", "") + f.suffix
            f.rename(PROTO_OUTPUT_DIR / new_name)


if __name__ == "__main__":
    protoc_exe = "protoc"
    main(protoc_exe)
