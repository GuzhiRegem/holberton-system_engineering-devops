#estoy con el proyecto final, la guanji es la guanji

exec{ 'fix-file':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
  path    => '/bin';
}
