import os
from datetime import datetime
import pandas as pd

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

def get_prep_df(prep_id, path='data/processed'):
	x_train = pd.read_csv(f"{path}/{prep_id}/x_train.csv")
	x_test = pd.read_csv(f"{path}/{prep_id}/x_test.csv")
	y_train = pd.read_csv(f"{path}/{prep_id}/y_train.csv")
	y_test = pd.read_csv(f"{path}/{prep_id}/y_test.csv")
	return x_train, y_train, x_test, y_test


# --- TUNNING --- #

def tunning_results(study, path):
	import optuna 
	import json
	
	path_to_save = f"{path}/{get_nb_name()}/tunning"
	os.makedirs(path_to_save, exist_ok=True)
	
	tunning_results = {}
	tunning_results['best_params'] = study.best_params
	tunning_results['best_value'] = study.best_value
	tunning_results['metric_names'] = study.metric_names

	with open(f"{path_to_save}/tunning_results.json", "w") as f:
		json.dump(tunning_results, f)

	study.trials_dataframe().to_csv(f"{path_to_save}/tunning_trials.csv", index=False)

	optuna.visualization.plot_edf(study).write_image(f"{path_to_save}/edf.png")
	optuna.visualization.plot_optimization_history(study).write_image(f"{path_to_save}/plot_optimization_history.png")
	optuna.visualization.plot_param_importances(study).write_image(f"{path_to_save}/plot_param_importances.png")
	optuna.visualization.plot_contour(study).write_image(f"{path_to_save}/plot_contour.png")

	print(f"Results saved in {path_to_save}")

	return tunning_results


