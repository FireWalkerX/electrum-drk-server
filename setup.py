from setuptools import setup

setup(
    name="electrum-drk-server",
    version="0.9",
    scripts=['run_electrum_drk_server','electrum-drk-server'],
    install_requires=['plyvel','jsonrpclib', 'irc'],
    package_dir={
        'electrumdrkserver':'src'
        },
    py_modules=[
        'electrumdrkserver.__init__',
        'electrumdrkserver.utils',
        'electrumdrkserver.storage',
        'electrumdrkserver.deserialize',
        'electrumdrkserver.networks',
        'electrumdrkserver.blockchain_processor',
        'electrumdrkserver.server_processor',
        'electrumdrkserver.processor',
        'electrumdrkserver.version',
        'electrumdrkserver.ircthread',
        'electrumdrkserver.stratum_tcp',
        'electrumdrkserver.stratum_http'
    ],
    description="Darkcoin Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU Affero GPLv3",
    url="https://github.com/testalt/electrum-drk-server/",
    long_description="""Server for the Electrum Lightweight Darkcoin Wallet"""
)


