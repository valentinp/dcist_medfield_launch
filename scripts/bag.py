#!/usr/bin/env python
""" Record the topics in topics.yaml to a bag file
"""

import rospy
import rospkg
import rosparam
import yaml
import argparse
import subprocess
import os
from datetime import datetime

def get_args():
    parser = argparse.ArgumentParser(description='Record the topics in {PACKAGE}/config/topics.yaml')
    parser.add_argument('--robot', required=True, help='Robot name (used to namespace topics appropriately)')
    parser.add_argument('--prefix', required=False, help='Prefix to prepend to the bag file.')
    parser.add_argument('--config', required=False, default="topics.yaml", help='Prefix to prepend to the bag file.')
    return parser.parse_known_args()[0]

def leading_slash(string):
    # prepend a leading slash to the given string, if it's missing
    return ("/" + string if string[0]!="/" else string)

if __name__=="__main__":
    args = get_args()

    # instantiate rospack
    rospack = rospkg.RosPack()
    rospy.loginfo("Recording topics from {}".format("/config" + args.config))
    topics_path = rospack.get_path("capstone_launch") + "/config/" + args.config

    # import and parse topics
    if not os.path.isfile(topics_path):
        rospy.logerr("Unable to find topics.yaml; no such file {}".format(topics_path))
    with open(topics_path, 'r') as topics:
        base_topics = yaml.safe_load(topics)

    # apply robot name prefix to topics (those that aren't raw)
    topics_to_record = ""
    for topic in base_topics["RAW"]:
        topics_to_record += " " + leading_slash(topic)
    for topic in base_topics["ROBOT_NAME"]:
        topics_to_record += " " + leading_slash(args.robot) + leading_slash(topic)
    
    # construct bag/yaml name
    output = (args.prefix + "_") if args.prefix else ""  
    output += datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    # dump all current ros params:
    rosparam.dump_params(output + ".yaml", "/")

    # actually rosbag record
    cmd = "rosbag record " + topics_to_record + " --lz4 -O {}.bag".format(output)
    rospy.loginfo("Calling {}".format(cmd))
    subprocess.call(cmd, shell=True)

