# -*- mode: python -*-

block_cipher = None


a = Analysis(['..\\..\\src\\main\\python\\main.py'],
             pathex=['D:\\python\\pyQTʵ��\\target\\PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='Myapp',
          debug=False,
          strip=False,
          upx=False,
          console=False , icon='D:\\python\\pyQTʵ��\\src\\main\\icons\\Icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='Myapp')
