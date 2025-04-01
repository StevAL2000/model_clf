@echo off
:: Setup script to install required Python packages with specific versions

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and try again.
    exit /b 1
)

:: Upgrade pip to the latest version
echo Upgrading pip...
python -m pip install --upgrade pip

:: Install required packages with specific versions
echo Installing required packages...
python -m pip install absl-py==2.1.0 aiohappyeyeballs==2.4.4 aiohttp==3.11.11 aiosignal==1.3.2 alembic==1.14.1 antlr4-python3-runtime==4.9.3 anyio==4.7.0 asteroid-filterbanks==0.4.0 astunparse==1.6.3 attrs==24.3.0 certifi==2024.12.14 cffi==1.17.1 charset-normalizer==3.4.1 click==8.1.8 colorama==0.4.6 colorlog==6.9.0 contourpy==1.3.1 cycler==0.12.1 dateparser==1.2.0 docopt==0.6.2 einops==0.8.0 ffmpeg==1.4 filelock==3.17.0 flatbuffers==25.1.24 fonttools==4.55.3 frozenlist==1.5.0 fsspec==2024.12.0 gast==0.6.0 greenlet==3.1.1 grpcio==1.70.0 h11==0.14.0 h5py==3.12.1 httpcore==1.0.7 httpx==0.28.1 huggingface-hub==0.28.0 HyperPyYAML==1.2.2 idna==3.10 imbalanced-learn==0.13.0 imblearn==0.0 Jinja2==3.1.5 joblib==1.4.2 julius==0.2.7 keras==3.8.0 keras-tuner==1.4.7 keras-utils==1.0.13 kiwisolver==1.4.8 kt-legacy==1.0.5 libclang==18.1.1 lightning==2.5.0.post0 lightning-utilities==0.11.9 llvmlite==0.44.0 Mako==1.3.8 Markdown==3.7 markdown-it-py==3.0.0 MarkupSafe==3.0.2 matplotlib==3.10.0 mdurl==0.1.2 ml-dtypes==0.4.1 mplfinance==0.12.10b0 mpmath==1.3.0 multidict==6.1.0 namex==0.0.8 networkx==3.4.2 noisereduce==3.0.3 numba==0.61.0 numpy==2.0.2 omegaconf==2.3.0 opt_einsum==3.4.0 optree==0.14.0 optuna==4.2.0 packaging==24.2 pandas==2.2.3 pandas_ta==0.3.14b0 patsy==1.0.1 pillow==11.1.0 pip==25.0 pocketsphinx==5.0.4 primePy==1.3 propcache==0.2.1 protobuf==5.29.3 pyannote.audio==3.3.2 pyannote.core==5.0.0 pyannote.database==5.1.3 pyannote.metrics==3.2.1 pyannote.pipeline==3.0.1 pycparser==2.22 pycryptodome==3.21.0 pydub==0.25.1 Pygments==2.19.1 pynndescent==0.5.13 pyparsing==3.2.1 python-binance==1.0.27 python-dateutil==2.9.0.post0 python-telegram-bot==21.10 pytorch-lightning==2.5.0.post0 pytorch-metric-learning==2.8.1 pytz==2024.2 PyYAML==6.0.2 regex==2024.11.6 requests==2.32.3 rich==13.9.4 ruamel.yaml==0.18.10 ruamel.yaml.clib==0.2.12 scikit-learn==1.6.1 scipy==1.15.1 seaborn==0.13.2 semver==3.0.4 sentencepiece==0.2.0 setuptools==75.8.0 shellingham==1.5.4 six==1.17.0 sklearn-compat==0.1.3 sniffio==1.3.1 sortedcontainers==2.4.0 SQLAlchemy==2.0.37 srt==3.5.3 statsmodels==0.14.4 sympy==1.13.1 tabulate==0.9.0 tensorboard==2.18.0 tensorboard-data-server==0.7.2 tensorboardX==2.6.2.2 tensorflow==2.18.0 tensorflow_intel==2.18.0 tensorflow_keras==0.1 termcolor==2.5.0 threadpoolctl==3.5.0 torch==2.5.1 torch_pitch_shift==1.2.5 torchmetrics==1.6.1 tqdm==4.67.1 typer==0.15.1 typing_extensions==4.12.2 tzdata==2024.2 tzlocal==5.2 umap==0.1.1 umap-learn==0.5.7 urllib3==2.3.0 vosk==0.3.45 websockets==14.1 Werkzeug==3.1.3 wheel==0.45.1 wrapt==1.17.2 xgboost==2.1.4 yarl==1.18.3

if %errorlevel% neq 0 (
    echo Failed to install some packages. Please check the error messages above.
    exit /b 1
)

echo All packages installed successfully.
pause