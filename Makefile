export MODEL_BASENAME=winterboot
export REPO_NAME=winterboot
export GITHUB_ORGANIZATION=kode-konveyor

include /usr/local/toolchain/rules.python

publish_release: compile
    python3 -m twine upload dist/*

