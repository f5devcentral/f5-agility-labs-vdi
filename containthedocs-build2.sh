#!/usr/bin/env bash

set -x

COMMAND="make -C docs html"

. ./containthedocs-image

exec docker run --rm \
  -v %cd%:/data --workdir "/data" \
  ${DOCKER_RUN_ARGS} \
  -e "LOCAL_USER_ID=$(id -u)" \
  ${DOC_IMG} ${COMMAND}
