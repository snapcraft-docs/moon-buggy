Summary: Drive some car across the moon
Name: moon-buggy
Copyright: GPL
Group: Amusements/Games
Version: 0.4.0.90
Release: 1
Source: moon-buggy-0.4.0.90.tar.gz
BuildRoot: /tmp/moon-buggy
%description
Moon-buggy is a simple character graphics game, where you drive some
kind of car across the moon's surface.  Unfortunately there are
dangerous craters there.  Fortunately your car can jump over them!

%prep
%setup

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s ./configure --sharedstatedir=/var/games --with-setgid=games
make

%install
make DESTDIR=${RPM_BUILD_ROOT} install-binPROGRAMS install-binSCRIPTS
make DESTDIR=${RPM_BUILD_ROOT} install-info-am install-man install-data-local

%post
if test "xgames" != "x"; then \
  chown "games" "/usr/local/bin/moon-buggy" \
    && chmod u+s "/usr/local/bin/moon-buggy" ; \
fi
chmod go-x "/usr/local/bin/maint-buggy"
if /bin/sh -c 'install-info --version | sed 1q | fgrep -s -v -i debian' >/dev/null 2>&1; then \
  list='moon-buggy.info'; \
  for file in $list; do \
    echo " install-info --info-dir=/usr/local/info /usr/local/info/$file";\
    install-info --info-dir=/usr/local/info /usr/local/info/$file || :;\
  done; \
else : ; fi
if test "xgames" != "x"; then \
  chown "games" "/var/games/moon-buggy" \
    && { test ! -f "/var/games/moon-buggy/mbscore" \
         || chown "games" "/var/games/moon-buggy/mbscore" ; } \
    && { test ! -f "/var/games/moon-buggy/mbscore" \
         || chmod go-w "/var/games/moon-buggy/mbscore" ; } \
    && chmod go-w "/var/games/moon-buggy" ; \
fi

%preun
cd /usr/local/info; \
if /bin/sh -c 'install-info --version | sed 1q | fgrep -s -v -i debian' >/dev/null 2>&1; then \
  ii=yes; \
else ii=; fi; \
list='moon-buggy.info'; \
for file in $list; do \
  test -z "i" \
    || install-info --info-dir=/usr/local/info --remove $file; \
done

%files
/usr/local/bin/moon-buggy
/usr/local/bin/maint-buggy
/usr/local/info/moon-buggy.info
/usr/local/man/man6/moon-buggy.6
/usr/local/man/man6/maint-buggy.6
/var/games/moon-buggy