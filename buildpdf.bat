docker run --rm -it -e LOCAL_USER_ID=1138664 -v %cd%:/data -w /data 0xhiteshpatel/containthedocs:2.3 make -C docs latexpdf
