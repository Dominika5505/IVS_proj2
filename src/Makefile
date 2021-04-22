STUFF_TO_CLEAN=__pycache__
APP=app
PACK_BATCH=pack
CODE_LANG=py
PROFILING_APP=profiling
PROFILING_INPUT=input_prof_1000_nums
HELP_FILE=help.txt

all: run
pack:
	${PACK_BATCH}.bat
clean:
	rd ${STUFF_TO_CLEAN} /q /s
run:
	${CODE_LANG} ${APP}.${CODE_LANG}
profile:
	${CODE_LANG} ${PROFILING_APP}.${CODE_LANG} <${PROFILING_INPUT}.txt
help:
	type ${HELP_FILE}