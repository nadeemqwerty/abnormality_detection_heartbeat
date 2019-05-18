from utils import transform_and_save_to_npy, transform_and_save_to_npy_1d, transform_and_save_to_npy_1d_part

transform_and_save_to_npy(["data/set_a/**","data/set_b/**"],"data/")
transform_and_save_to_npy_1d(["data/set_a/**","data/set_b/**"],"data/")

transform_and_save_to_npy_1d_part(["data/set_a/**","data/set_b/**"],"data/")
