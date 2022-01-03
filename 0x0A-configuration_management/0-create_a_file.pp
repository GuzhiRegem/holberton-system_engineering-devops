file { '/tmp/school':
	mode => '/tmp/school',
	owner => 'www-data',
	group => 'www-data',
	content => 'I love Puppet'
}
