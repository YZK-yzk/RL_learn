import numpy as np
import sys
from six import StringIO, b

from gym import utils
from gym.envs.toy_text import discrete


import tensorflow as tf
from numpy import *
a= tf.placeholder(tf.int32,shape=[None,1])
y=tf.layers.dense(a,10)

