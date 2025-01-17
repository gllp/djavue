#!/bin/bash
RESTORE='\033[0m'
RED='\033[00;31m'
GREEN='\033[00;32m'
YELLOW='\e[0;33m'
HOST_PROD=buser_project.myexample.io

# Because nobody wants to be memorizing commands all the time
# Instructions:
# 1) ". dev.sh"
# 2) "devhelp"
# 3) Be happy


workon buser_project  # Change this to your project's name

export PROJ_BASE="$(dirname "${BASH_SOURCE[0]}")"
CD=$(pwd)
cd $PROJ_BASE
export PROJ_BASE=$(pwd)
cd $CD

#. ci/funcs.sh

function devhelp {
    echo -e "${GREEN}devhelp${RESTORE}           Prints this ${RED}help${RESTORE}"
    echo -e ""
    echo -e "${GREEN}pytests${RESTORE}           Runs python ${RED}tests${RESTORE}"
    echo -e ""
    echo -e "${GREEN}pycoverage${RESTORE}        Generates python ${RED}test coverage${RESTORE} report"
    echo -e ""
    echo -e "${GREEN}runflake8${RESTORE}         Runs ${RED}PEP8${RESTORE} against python code"
    echo -e ""
    echo -e "${GREEN}djangorun${RESTORE}         Runs ${RED}django${RESTORE} backend"
    echo -e ""
    echo -e "${GREEN}dkbuild${RESTORE}           Builds a ${RED}docker image${RESTORE} for this project"
    echo -e ""
    echo -e "${GREEN}dknpminstall${RESTORE}      Download node dependencies to ${RED}./node_modules/${RESTORE}"
    echo -e ""
    echo -e "${GREEN}dkup${RESTORE}              Starts a dockerized ${RED}full development environment${RESTORE}"
    echo -e ""
    echo -e "${GREEN}dk <command>${RESTORE}      Runs ${RED}<command>${RESTORE} inside main container"
    echo -e "                  Example:"
    echo -e "                   dk ${RED}bash${RESTORE}"
    echo -e ""
    echo -e "${GREEN}dkrun_prod${RESTORE}        Starts django and nuxt (dockerized) in production mode"
    echo -e ""
    echo -e "${GREEN}deploy_prod${RESTORE}       Connects to the production server and deploys it"
    echo -e ""
    echo -e "${GREEN}dkpgnginx${RESTORE}         Starts dockerized ${RED}nginx and postgres${RESTORE}"
    echo -e ""
    echo -e "${GREEN}sudo_${RESTORE}${RED}<DOCKER_FUNCTION_NAME>${RESTORE} Same docker commands as described above, but using sudo"
    echo -e ""
}

function pytests {
    CD=$(pwd)
    cd $PROJ_BASE
    ./manage.py test core --parallel 4
    exitcode=$?
    cd $CD
    return $exitcode
}

function pycoverage {
    CD=$(pwd)
    cd $PROJ_BASE
    coverage run --source='core,commons' --omit='core/tests/**,core/migrations/**' manage.py test --noinput
    exitcode=$?
    coverage html
    cd $CD
    return $exitcode
}

function djangorun {
    CD=$(pwd)
    cd $PROJ_BASE
    ./manage.py runserver
    exitcode=$?
    cd $CD
    return $exitcode
}

function dkbuild {
    CD=$(pwd)
    cd $PROJ_BASE
    docker build -t buser_project .
    exitcode=$?
    cd $CD
    return $exitcode
}

function dknpminstall {
    CD=$(pwd)
    cd $PROJ_BASE
    docker run -it --rm -v $(pwd):/app -w /app/frontend -e NODE_ENV=development buser_project npm install
    exitcode=$?
    cd $CD
    return $exitcode
}

function dkpgnginx {
    CD=$(pwd)
    cd $PROJ_BASE
    docker-compose -f docker/compose/pgnginx.yaml up
    exitcode=$?
    cd $CD
    return $exitcode
}

function dkup {
    CD=$(pwd)
    cd $PROJ_BASE
    docker-compose -f docker/compose/dev.yaml up
    exitcode=$?
    cd $CD
    return $exitcode
}

function dkrun_prod {
    docker stop buser_project
    docker rm buser_project
    docker run --name buser_project -d --env-file /home/ubuntu/buser_project.env \
        -p 3000:3000 -p 8000:8000 \
        -v /home/ubuntu/dkdata/buser_project:/dkdata \
        buser_project start_web.sh
}

function deploy_prod {
  ssh ubuntu@$HOST_PROD "
    cd ~/djavue
    git reset --hard
    git pull
    source buserProject/dev.sh
    dkbuild
    dkrun_prod
  "
}

function dk {
    docker exec -it buser_project $@
}

function sudo_dkbuild {
    CD=$(pwd)
    cd $PROJ_BASE
    sudo docker build -t buser_project .
    exitcode=$?
    cd $CD
    return $exitcode
}

function sudo_dknpminstall {
    CD=$(pwd)
    cd $PROJ_BASE
    sudo docker run -it --rm -v $(pwd):/app -w /app/frontend -e NODE_ENV=development buser_project npm install
    exitcode=$?
    cd $CD
    return $exitcode
}

function sudo_dkpgnginx {
    CD=$(pwd)
    cd $PROJ_BASE
    sudo docker-compose -f docker/compose/pgnginx.yaml up
    exitcode=$?
    cd $CD
    return $exitcode
}

function sudo_dkup {
    CD=$(pwd)
    cd $PROJ_BASE
    sudo docker-compose -f docker/compose/dev.yaml up
    exitcode=$?
    cd $CD
    return $exitcode
}

function sudo_dk {
    sudo docker exec -it buser_project $@
}

function runflake8 {
    CD=$(pwd)
    cd $PROJ_BASE
    flake8 .
    exitcode=$?
    cd $CD
    return $exitcode
}

function echo_red {
    echo -e "\e[31m$1\e[0m";
}

function echo_green {
    echo -e "\e[32m$1\e[0m";
}

function echo_yellow {
    echo -e "${YELLOW}$1${RESTORE}";
}

echo_green "Welcome to buser_project's dev env"
echo_green "Hint: autocomplete works for the commands below ;)"
echo_red   "------------------------------------------------------------------------"
devhelp
