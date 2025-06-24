# my-rules-dat
My rules dat for mihomo. Update weekly by using github actions.

# How To Use
```yaml
rule-providers:
  all:
    type: http
    path: ./all.yaml
    url: "https://github.com/h3ll0www0rld/my-rules-dat/releases/latest/download/all.yaml"
    # or using proxy
    # url: "https://ghfast.top/https://github.com/h3ll0www0rld/my-rules-dat/releases/latest/download/all.yaml"
    interval: 604800
    behavior: classical
    format: yaml

  reward:
    type: http
    path: ./reward.yaml
    url: "https://github.com/h3ll0www0rld/my-rules-dat/releases/latest/download/reward.yaml"
    # or using proxy
    # url: "https://ghfast.top/https://github.com/h3ll0www0rld/my-rules-dat/releases/latest/download/reward.yaml"
    interval: 604800
    behavior: classical
    format: yaml

  fz:
    type: http
    path: ./fz.yaml
    url: "https://github.com/h3ll0www0rld/my-rules-dat/releases/latest/download/fz.yaml"
    # or using proxy
    # url: "https://ghfast.top/https://github.com/h3ll0www0rld/my-rules-dat/releases/latest/download/fz.yaml"
    interval: 604800
    behavior: classical
    format: yaml
```

# Rules Come From
- [去广告](https://github.com/lingeringsound/10007/)
