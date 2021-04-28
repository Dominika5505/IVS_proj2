cd ..
git bundle create ./projGITrepo.bundle --all
set curDir=%cd%
cd ..
mkdir temp
cd temp
set tempDir=%cd%
mkdir xpucek03_xfojti15_xciesl06_xsedil00
cd xpucek03_xfojti15_xciesl06_xsedil00
mkdir repo
cd repo
set curDir2=%cd%
cd %curDir% 
xcopy ".\*" "%curDir2%" /E /H /C /I
cd %curDir2%
del /F *.zip
cd ..
mkdir doc
mkdir install
cd doc
set docDir=%cd%
cd ..
cd install
set installDir=%cd%
cd ..
cd ..
cd ..
xcopy ".\doc\*" "%docDir%" /E /H /C /I
xcopy ".\install\*" "%installDir%" /E /H /C /I
attrib "%curDir2%\.git" -s -h
powershell -nologo -noprofile -command "& {Compress-Archive '%tempDir%\*' -DestinationPath '%curDir%\xpucek03_xfojti15_xciesl06_xsedil00.zip' -Force}"
cd %curDir2%
cd .. 
cd ..
cd ..
rd temp /q /s
cd %curDir%
del /F *.bundle