# using Puppet to configure a server

$content="server_name _;\n\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\
        \n\t\tindex index.html index.htm;\n\t}\n"

exec { 'apt_update':
command => '/usr/bin/sudo /usr/bin/apt-get update'
}

package { 'nginx':
  ensure => installed,
}

file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/shared', '/data/web_static/releases/test']:
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => "<html>\n<head>\n</head>\n<body>\n<h1>Welcome to web_static deployment!</h1>\n</body>\n</html>",
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
}

file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
  force  => true,
}

file { '/data':
  ensure  => directory,
  recurse => true,
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

file_line { 'nginx-config':
  path  => '/etc/nginx/sites-available/default',
  line  => $content,
  match => 'server_name _;',
}

service { 'nginx':
  ensure => running,
  enable => true,
  subscribe => File_line['nginx-config'],
}

