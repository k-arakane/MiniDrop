FROM --platform=linux/amd64 condaforge/miniforge3:25.3.0-3

COPY environment.yaml /tmp/environment.yaml

RUN <<EOF
mamba env create -yf /tmp/environment.yaml
conda clean -afy
rm -rf /tmp/environment.yaml
EOF

RUN echo "conda activate minidrop" >> ~/.bashrc
