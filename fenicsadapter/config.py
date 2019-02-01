"""This is configuration module of fenicsadapter."""

import os, sys, json

class Config:
    """Handles reading of config. parameters of the fenicsadapter based on JSON
    configuration file. Initializer calls readJSON() method. Instance attributes
    can be accessed by provided getter functions.

    :param adapter_config_filename: name of the adapter configuration file
    :ivar _config_file_name: name of the preCICE configuration file
    :ivar _solver_name : name of the solver
    :ivar _coupling_mesh_name: name of mesh as defined in preCICE config
    :ivar _read_data_name: name of read data as defined in preCICE config
    :ivar _write_data_name: name of write data as defined in preCICE config
    :ivar _N_this: waveform relaxation substeps for this participant
    :ivar _N_other: waveform relaxation substeps for other participant
    """

    def __init__(self, adapter_config_filename):

        self._config_file_name = None
        self._solver_name = None
        self._coupling_mesh_name = None
        self._read_data_name = None
        self._write_data_name = None
        self._N_this = None
        self._N_other = None

        self.readJSON(adapter_config_filename)

    def readJSON(self, adapter_config_filename):
        """ Reads JSON adapter configuration file and saves the data to
        the respective instance attributes.

        :var path: stores path to the JSON config file
        :var data: data decoded from JSON files
        :var read_file: stores file path
        """

        path = os.path.join(os.getcwd(), os.path.dirname(sys.argv[0]), adapter_config_filename)
        read_file = open(path, "r")
        data = json.load(read_file)

        self._config_file_name = data["config_file_name"]
        self._solver_name = data["solver_name"]
        self._coupling_mesh_name = data["interface"]["coupling_mesh_name"]
        self._write_data_name = data["interface"]["write_data_name"]
        self._read_data_name = data["interface"]["read_data_name"]
        # todo check that either both keys (N_this and N_other) exist or not.
        try:
            self._N_this = data["interface"]["N_this"]
            assert(self._N_this > 0)
        except KeyError:
            self._N_this = None
        try:
            self._N_other = data["interface"]["N_other"]
            assert (self._N_other > 0)
        except KeyError:
            self._N_this = None
        read_file.close()

    def get_config_file_name(self):
        return self._config_file_name

    def get_solver_name(self):
        return self._solver_name

    def get_coupling_mesh_name(self):
        return self._coupling_mesh_name

    def get_read_data_name(self):
        return self._read_data_name

    def get_write_data_name(self):
        return self._write_data_name