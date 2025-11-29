###################################################################
# Base stage to prep a shared base image for build, test and run
#
FROM python:3.15.0a2-slim-bookworm AS base

WORKDIR /app

RUN mkdir -p /dist

# JIRA-XXXX build-essentials and pg dependencies should only go in the build stage but wheels are build from source
RUN apt-get -y update &&  \ 
    apt-get install -y --no-install-recommends  \
    build-essential \
    postgresql \
    postgresql-contrib \
    libpq-dev 

###################################################################
# Build stage to product the wheel artifact
#
FROM base AS build

# Copies too much but since we only pick the wheel from the build it doesn't matter
COPY . .

RUN pip install --no-cache-dir build==1.3.0 && \
    python -m build --verbose --wheel

###################################################################
# Test stage
#

FROM build AS test

# Install the package including test dependencies
RUN pip install -e '.[develop]'

RUN pytest . -vv

###################################################################
# Run stage installs the wheel in a clean image to run for production
#

FROM base AS run

# Intake of the app (wheel)
COPY --from=build /app/dist/* /dist
RUN pip install --no-cache-dir pytest /dist/*.whl

# Copy the migrations into the workdir
COPY jaga/migrations migrations

# JIRA-XXX Add cleanup image

COPY entrypoint.sh /
RUN chmod u+x /entrypoint.sh

CMD ["/entrypoint.sh"]
