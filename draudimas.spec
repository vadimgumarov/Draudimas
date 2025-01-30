# draudimas.spec
from PyInstaller.utils.hooks import collect_all

# Get all the data for our packages
datas = []
binaries = []
hiddenimports = []

# Collect all necessary data for python-docx
docx_datas, docx_binaries, docx_hiddenimports = collect_all('docx')
datas.extend(docx_datas)
binaries.extend(docx_binaries)
hiddenimports.extend(docx_hiddenimports)

# Add explicit python-docx imports
hiddenimports.extend([
    'docx',
    'docx.document',
    'docx.oxml',
    'docx.oxml.shared',
    'docx.oxml.text',
    'docx.table',
    'lxml',
    'lxml.etree',
    'lxml._elementpath'
])

# Collect all necessary data for PyMuPDF (fitz)
fitz_datas, fitz_binaries, fitz_hiddenimports = collect_all('fitz')
datas.extend(fitz_datas)
binaries.extend(fitz_binaries)
hiddenimports.extend(fitz_hiddenimports)

a = Analysis(
    ['draudimas.py'],
    pathex=[],
    binaries=binaries,
    datas=datas + [
        ('templates', 'templates'),  # Include templates directory
        ('cases', 'cases'),         # Include cases directory
        ('src', 'src'),            # Include source files
    ],
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='draudimas',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)