import subprocess32

from app import app


# Utility Functions
def compass_compile(app_dir):
    """
    Use this to recompile sass into css
    :param app_dir:
    """
    with subprocess32.Popen(['compass', 'compile'],
                            stdout=subprocess32.PIPE, stderr=subprocess32.PIPE, cwd=app_dir) as p:
        stdout, stderr = p.communicate()
        if stdout or stderr:
            print "-- COMPASS SAYS --", stderr.decode(errors='replace'), stdout.decode(errors='replace')
        else:
            print "No Compass Updates"


if __name__ == '__main__':
    compass_compile(app.config['APP_DIR'])
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'],
            extra_files=app.config['EXTRA_FILES'])
