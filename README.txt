# build sample file
podman build -t pysample .

#and now ready to run!
podman run --rm pysample

#pass arguments via env variables
podman run --rm -e "parg1=time" pysample

