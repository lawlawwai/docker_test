import configparser
import redis
global redis1


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    global redis1
    redis1 = redis.Redis(host=(config['REDIS']['HOST']), password=(config['REDIS']['PASSWORD']),
                         port=(config['REDIS']['REDISPORT']), username="lawlawwai")
    keys = redis1.keys("*")
    reply = redis1.acl_users()[0]+"\n"
    for key in keys:
        k = key.decode('UTF-8')
        reply = reply + k + " : " + redis1.get(k).decode('UTF-8') + "\n"
    print(reply)


if __name__ == '__main__':
    main()
