from dataset import EyeStateDataset
from nets import EyeStateNet
import argparse
def get_cmd_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--dataset_dir",default="",type=str)
    parser.add_argument("--left",type=bool)
    parser.add_argument("--epochs",default=10,type=int)
    parser.add_argument("--batch_size",default=32,type=int)
    parser.add_argument("--lr",default=1e-4,type=float)
    parser.add_argument("--steps",default=200,type=int)
    parser.add_argument("--weights",default=None,type=str)
    parser.add_argument("--output",default=None,type=str)
    args = parser.parse_args()
    return args

def main():
    args = get_cmd_args()
    dataset = EyeStateDataset(args.dataset_dir,image_shape=(24,24),left_eye=args.left)
    dataset.load_dataset()
    net = EyeStateNet(dataset,left_eye=args.left,
            epochs=args.epochs,batch_size=args.batch_size,lr=args.lr,steps_per_epoch=args.steps,
            weights=args.weights,output=args.output)
    net.train()

if __name__ == "__main__":
    main()
