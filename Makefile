# Most x7 projects don't need a unique makefile
include ../x7-lib/common.mk

# Exclude things that don't need autodoc
DOCS_EXCLUDE := x7/lib/utils/*
COVERAGE_OMIT := --omit "x7/lib/utils/*"

# Turn off dev_update for x7-lib
DEV_UPDATE :=
