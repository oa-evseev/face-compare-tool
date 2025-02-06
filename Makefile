PYTHON := python3
VENV := .venv
SRC := face_compare.py
DIST := dist/

.PHONY: install run build build-windows build-macos build-linux clean

install:
	$(PYTHON) -m venv $(VENV)
	. $(VENV)/bin/activate && pip install -r requirements.txt

run:
	. $(VENV)/bin/activate && streamlit run $(SRC)

build:
	pyinstaller --onefile --noconsole $(SRC)

build-windows:
	pyinstaller --onefile --noconsole --name face_compare.exe $(SRC)

build-macos:
	pyinstaller --onefile --windowed --name face_compare $(SRC)

build-linux:
	pyinstaller --onefile --name face_compare $(SRC)

clean:
	rm -rf build $(DIST) *.spec $(VENV)

