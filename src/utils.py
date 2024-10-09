import os
from datetime import datetime
# --- UTILS ---

def get_nb_name():
	"""Get the name of the current notebook. Only works in Jupyter notebooks and VSCode."""
	from IPython import get_ipython
	
	ip = get_ipython()
	path = None
	if '__vsc_ipynb_file__' in ip.user_ns:
		path = ip.user_ns['__vsc_ipynb_file__']

	return os.path.splitext(os.path.basename(path))[0]


# --- LOADERS --- #

def save_prep_data_4(x_train, x_test, y_train, y_test, path='data/processed'):
	path_prep_data = f'{path}/{get_nb_name()}'
	os.makedirs(path_prep_data, exist_ok=True)
	x_train.to_csv(f'{path_prep_data}/x_train.csv', index=False)
	x_test.to_csv(f'{path_prep_data}/x_test.csv', index=False)
	y_train.to_csv(f'{path_prep_data}/y_train.csv', index=False)
	y_test.to_csv(f'{path_prep_data}/y_test.csv', index=False)
	return print(f"Data saved in {path_prep_data}")


