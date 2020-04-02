ROUTES = {
    "server": {
        "start": "game-servers/{}/start",
        "restart": "game-servers/{}/reset",
        "create": "game-servers",
        "stop": "game-servers/{}/stop",
        "delete": "game-servers/{}",
        "get": "game-servers/{}",
        "list": "game-servers",
        "metrics": "game-servers/{}/metrics",
        "clone": "game-servers/{}/duplicate",

        "file": {
            "delete": "game-servers/{}/files/{}",
            "sync": "game-servers/{}/sync-files",
            "upload": "game-servers/{}/files/{}",
            "unzip": "game-servers/{}/unzip/{}",
            "list": "game-servers/{}/files",
            "download": "game-servers/{}/files/{}",
        },

        "console": {
            "get": "game-servers/{}/console",
            "send": "game-servers/{}/console",
        },

        "ftp_password_reset": "game-servers/{}/regenerate-ftp-password",
    },

    "domains": "custom-domains",

    "account": "account",
}