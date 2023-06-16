---
title: Deployment
layout: default
nav_order: 6
---

# Deployment

{: .warning }
Diplomatik is meant to be run as a non-public backend service where API payloads can be proxied to it directly.
Typically this would be another web server. Since it currently doesn't provide any authentication or authorization, it
is up to the proxy service to handle that.

Diplomatik is provided as a self-hosted Docker container. You can take a look at the 
[get started guide](https://fretz12.github.io/diplomatik/get_started.html) on a demo launch. There is a 
production Docker compose file sample located at `deployment/docker/prod/docker-compose.yml`. Adjust it as needed.
