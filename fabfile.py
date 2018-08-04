from fabric.api import local, run, cd, env, put, roles


env.user = 'ethanc'
env.hosts = []

env.roledefs = {
    'server': ['192.168.1.122'],
}


def pack():
    local('python setup.py sdist --formats=gztar', capture=False)


@roles('server')
def deploy():
    dist = local('python setup.py --fullname', capture=True).strip()
    put('dist/%s.tar.gz' % dist, '/tmp/cs3.tar.gz')
    run('mkdir /tmp/cs3')
    with cd('/tmp/cs3'):
        run('tar xzf /tmp/cs3.tar.gz')
        with cd('/tmp/cs3/%s' % dist):
            run('sudo /home/ethanc/pyenv2/bin/python setup.py install')
    run('sudo rm -rf /tmp/cs3 /tmp/cs3.tar.gz')
    run('rm -rf /home/ethanc/cs3/static/xadmin')
    run('ln -s /home/ethanc/pyenv2/lib/python2.7/site-packages/%s-py2.7.egg/extra_apps/xadmin/static/xadmin/ /home/ethanc/cs3/static/' % dist)
#     run('sudo service apache2 restart')
    # run('touch /var/www/wiki/wiki.wsgi')
