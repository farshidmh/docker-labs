FROM scottyhardy/docker-wine
CMD rm -rf $HOME/.wine
ENV WINEARCH=win32
RUN winetricks -q ie6
ENTRYPOINT wine iexplore

