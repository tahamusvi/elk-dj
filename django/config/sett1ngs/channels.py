from .base import *

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.pubsub.RedisPubSubChannelLayer",
        "CONFIG": {
            "hosts": [
                {
                    "address": REDIS_LINK,
                }
            ]
        },
    }
}
