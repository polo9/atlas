

def cleanup():
    import shutil
    from os import getcwd, remove
    from os.path import isdir
    from glob import glob
    from foundations_contrib.global_state import foundations_context
    from foundations_internal.foundations_context import FoundationsContext

    tmp_dir = getcwd() + '/foundations_home/job_data'
    if isdir(tmp_dir):
        shutil.rmtree(tmp_dir)

    for file in glob('*.tgz'):
        remove(file)

    foundations_context = FoundationsContext()
