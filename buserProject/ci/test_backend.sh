#!/bin/bash
docker-compose -f docker/compose/test.yml run buser_project unittests.sh
exitcode=$?
docker-compose -f docker/compose/test.yml down
exit $exitcode
