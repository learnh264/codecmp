import argparse

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

parser = argparse.ArgumentParser(description='Produce BD score report')
parser.add_argument('--enc', default="resources/enc_x264.json",
        help='encoder configure json file')
parser.add_argument('--refs', default="resources/games.json",
        help='references configure json file or directorie')
parser.add_argument('--res', default="out_default/res/",
        help='final result save path')
parser.add_argument('--id', default="default",
        help='id of this run')
parser.add_argument('--resume', default=False, type=str2bool,
        help='continue the score process')

args = parser.parse_args()

