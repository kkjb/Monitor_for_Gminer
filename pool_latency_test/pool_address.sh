#!/bin/sh
./paping -p 4444 -c 4 asia2.ethermine.org   >asia2_tcp_main.txt;
./paping -p 4444 -c 4 asia1.ethermine.org   >asia1_tcp_main.txt;
./paping -p 4444 -c 4 eu1.ethermine.org     >eu1_tcp_main.txt                  ;
./paping -p 4444 -c 4 us1.ethermine.org     >us1_tcp_main.txt                  ;
./paping -p 4444 -c 4 us2.ethermine.org     >us2_tcp_main.txt                  ;

./paping -p 14444 -c 4 asia2.ethermine.org  >asia2_tcp_alt.txt                 ;
./paping -p 14444 -c 4 asia1.ethermine.org  >asia1_tcp_alt.txt                 ;
./paping -p 14444 -c 4 eu1.ethermine.org    >eu1_tcp_alt.txt                   ;
./paping -p 14444 -c 4 us1.ethermine.org    >us1_tcp_alt.txt                   ;
./paping -p 14444 -c 4 us2.ethermine.org    >us2_tcp_alt.txt                   ;

./paping -p 5555 -c 4 asia2.ethermine.org   >asia2_tcp_ssl.txt                 ;
./paping -p 5555 -c 4 asia1.ethermine.org   >asia1_tcp_ssl.txt                 ;
./paping -p 5555 -c 4 eu1.ethermine.org     >eu1_tcp_ssl.txt                   ;
./paping -p 5555 -c 4 us1.ethermine.org     >us1_tcp_ssl.txt                   ;
./paping -p 5555 -c 4 us2.ethermine.org     >us2_tcp_ssl.txt                   ;

./paping -p 6688 -c 4 eth.f2pool.com        >eth_f2pool_main.txt               ;
./paping -p 6688 -c 4 eth-backup.f2pool.com >eth_f2pool_alt.txt               ;

./paping -p 4444 -c 4 ru-eth.hiveon.net     >ru-eth.hiveon.net_main.txt        ;
./paping -p 4444 -c 4 eu-eth.hiveon.net     >eu-eth.hiveon.net_main.txt        ;
./paping -p 4444 -c 4 naw-eth.hiveon.net    >naw-eth.hiveon.net_main.txt       ;
./paping -p 4444 -c 4 aspac1-eth.hiveon.net >aspac1-eth.hiveon.net_main.txt    ;
./paping -p 14444 -c 4 hk-eth.hiveon.net     >hk-eth.hiveon.net_main.txt       ;
./paping -p 4444 -c 4 usw-eth.hiveon.net    >usw-eth.hiveon.net_main.txt       ;
./paping -p 4444 -c 4 use-eth.hiveon.net    >use-eth.hiveon.net_main.txt       ;

./paping -p 14444 -c 4 ru-eth.hiveon.net     >ru-eth.hiveon.net_alt.txt        ;
./paping -p 14444 -c 4 eu-eth.hiveon.net     >eu-eth.hiveon.net_alt.txt        ;
./paping -p 14444 -c 4 naw-eth.hiveon.net    >naw-eth.hiveon.net_alt.txt       ;
./paping -p 14444 -c 4 aspac1-eth.hiveon.net >aspac1-eth.hiveon.net_alt.txt    ;
./paping -p 8080 -c 4 hk-eth.hiveon.net     >hk-eth.hiveon.net_alt.txt         ;
./paping -p 14444 -c 4 usw-eth.hiveon.net    >usw-eth.hiveon.net_alt.txt       ;
./paping -p 14444 -c 4 use-eth.hiveon.net    >use-eth.hiveon.net_alt.txt       ;

./paping -p 24443 -c 4 ru-eth.hiveon.net     >ru-eth.hiveon.ssl.txt            ;
./paping -p 24443 -c 4 eu-eth.hiveon.net     >eu-eth.hiveon.ssl.txt            ;
./paping -p 24443 -c 4 naw-eth.hiveon.net    >naw-eth.hiveon.ssl.txt           ;
./paping -p 24443 -c 4 aspac1-eth.hiveon.net >aspac1-eth.hiveon.ssl.txt        ;
./paping -p 24443 -c 4 hk-eth.hiveon.net     >hk-eth.hiveon.ssl.txt            ;
./paping -p 24443 -c 4 usw-eth.hiveon.net    >usw-eth.hiveon.ssl.txt           ;
./paping -p 24443 -c 4 use-eth.hiveon.net    >use-eth.hiveon.ssl.txt           ;
