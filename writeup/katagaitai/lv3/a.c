#include <stdio.h>
#include <stdlib.h>
#include <err.h>
#include <sys/types.h>
#include <dirent.h>

int
main (int argc, char *argv[])
{
	int	i;

	const char *dirname = ".";
	struct dirent **namelist;
	int r = scandir(dirname, &namelist, NULL, NULL);
	if(r == -1) {
		err(EXIT_FAILURE, "%s", dirname);
	}
	(void) printf ("%d\n", r);
	for (i = 0; i < r; ++i) {
		(void) printf ("%s\n", namelist[i]->d_name);
		free(namelist[i]);
	}
	free(namelist);

	exit (EXIT_SUCCESS);
}