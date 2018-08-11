docker run --rm -it -e LOCAL_USER_ID=1138664 -v %cd%:/data -w /data f5devcentral/containthedocs:1.0.4_agility make -C docs html
