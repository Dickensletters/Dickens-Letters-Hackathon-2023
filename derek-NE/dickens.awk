#
# dickens.awk,  4 Feb 23

$1 == "</opener>" {
	getline
	gsub("^ *<p>", "", $0)
	gsub("</p>", "", $0)
	print $0
	next
	}

