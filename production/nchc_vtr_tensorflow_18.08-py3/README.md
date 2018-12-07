1. *nvcr.io/nvidia/tensorflow:18.10-py3* is required
2. `try.py` in execution mode and `requirement.txt` must in the same directory
3. use `sudo nvidia-docker build . -t nchc/vtr:20181113` to build image
4. run as `sudo nvidia-docker run -it -p 5000:5000 nchc/vtr:20181113`

