import pathlib, yaml
import selenium_loader

from yaml.loader import SafeLoader

if __name__ == '__main__':
  config = {}
  file = pathlib.Path("config/backup_download.yml")
  with open(file.absolute(), "r") as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)

  valid = selenium_loader.config.ConfigValidator.validate(config)
  print(valid)
