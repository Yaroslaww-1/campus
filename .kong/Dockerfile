FROM kong
ENV LUA_PATH /usr/local/share/lua/5.1/?.lua;/usr/local/kong-oidc/?.lua;;
# For lua-cjson
ENV LUA_CPATH /usr/local/lib/lua/5.1/?.so;;

# Install unzip for luarocks, gcc for lua-cjson
USER root
RUN apk update && apk add git unzip luarocks

# Install plugins
# RUN luarocks install kong-plugin-url-rewrite

USER kong
