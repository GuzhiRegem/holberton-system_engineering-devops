#puppet file

exec { 'pkill killmenow':
  provider => 'shell'
}
