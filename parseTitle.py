#!/usr/bin/env python
# coding: utf-8

import re

class parseTitle:
    def __init__(self,titles):
        self.seplist = re.compile(":\s|-based|(?:\s|^)(?:a|an|the|in|based on|on|to|of|with|without|by|from|for|via|toward|towards|beyond|using|and|or|as|is|am|are)(?:\s|$)",re.IGNORECASE)
        self.replist = re.compile("^\s|^(?:a|an|the|in)\s|\s(?:a|an|the|in)\s|[^si](s)$|^\s$|^in$",re.IGNORECASE)
        
        self.plist = "interaction|estimation|prediction|alignment|detection|recognition|classification|segmentation|\
identification|retrieval|generation|prediction|inpainting|labeling|distillation|visualizaton|reconstruction|enhancement|\
editing|idenfication|verification|authentication|restoration|tracking|matching|categorization|denoising|navigation|Attack|Grounding|amplification|Captioning|\
answering|answer|Recovery|Parsing|localization|retargeting|relocalization|Synthesis|Correction|Searching|search|compression|Rendering|DeepFake|Reading|\
benchmark|benchmarking|animation|Translation|music|fairness|responsible|trustworthy|pruning|question answer"
        self.pulist = "3d reconstruction|object detection|object recognition|object categorization|6d pose|face recognition|face detection|face verification|face identification|\
pedestrian detection|open dataset|knowledge distillation|style transfer|character recognition|character region detection|text spot|\
semantic segmentation|instance segmentation|image segmenation|object tracking|metric learning|pre training|fine tuning|fully convolutional network|Neural Radience Field|Light field|\
action recognition|re identification|image classification|deformable matching|deformable object|non rigid|weak supervision|transformer|auto encoder|decoder|\
knowledge transfer|domain adapation|domain adaptation|reinforcement learning|transfer learning|active learning|multi modal|cross modal|\
simultaneous localization and mapping|federated learning|point cloud|Siamese|wild|disentangl|E2E|end to end|spars|adversarial|weakly supervised|\
weak supervision|self supervis|one shot|few shot|zero shot|image generation|video generation|captioning|Differential privacy|\
diffusion|human computer interaction|attention|representation learning|contrastive learning|continual learning|incremental learning|meta learning|\
unsupervised|semi supervised|noisy label|soft label|deep neural network|boosting|boost|expert|spatio temporal|Bayesian|Bandit|Combinatorial|\
multi task learning|multiple instance learning|multi instance learning|Kullback Leibler|generative|LLM|Language Model|tuning|embedding|\
Curriculum|certification|equivariant|normalizing flow|world model|flow network|multi agent|long context|feature selection|model selection|data selection|subset selection|\
latent|quantum|low rank|instruction|label|submodular|Lipschitz|vision and language|visual language"
        self.mlist = "learning|clustering|graph|training|transfer|Defocus|Regression|supression|synthetic|resolution|adaptation|network|\
fusion|reasoning|topology|space|modeling|Feature|Generalization|Detector|variation|representation|\
classifier|recognizer|minimization|maxmization|Expression|label|Descriptor|extractor|regularization|quantization|coarse to fine|contrastive\
Independent Component"
        self.tlist = "3D|rgbd|video|frame|dataset|camera|infrared|depth|lider|3D|Text to Image|imagenet|wordnet"
        self.malist = "SLAM|CNN|R CNN|RCNN|RNN|LSTM|CTC|SOM|GAN|ICA|PCA|U NET|UNET|Nerf|SVM|Bagging|MOE|\
Random forest|RF|KL divergence|DNN|GBM|VAE|ODE|PDE|CLIP"

        self.matchlist = re.compile(self.plist+"|"+self.pulist+"|"+self.mlist+"|"+self.tlist,re.IGNORECASE)
        self.matchalist = re.compile(self.malist)

        self.titles = titles
        self.wordhist = {}

    def wordfreq(self):
        for title in self.titles:
            """
            sepwords = self.seplist.split(title)
            for item in sepwords:
                item = self.replist.sub("", item)
                item = re.sub( r'-' , " ", item )
                item = re.sub( r'&' , "and", item )
                item = re.sub( r'sation' , "zation", item )
                item = re.sub( r'ising' , "izing", item )
                #####
                words = self.matchlist.findall(item)
                if words:
                    for word in words:
                        if word in self.wordhist:
                            self.wordhist[word] += 1
                        else:
                            self.wordhist[word] = 1
                words = self.matchalist.findall(item)
                if words:
                    for word in words:
                        if word in self.wordhist:
                            self.wordhist[word] += 1
                        else:
                            self.wordhist[word] = 1
            """
            words = set(self.matchlist.findall(title))
            if words:
                for word in words:
                    if word in self.wordhist:
                        self.wordhist[word] += 1
                    else:
                        self.wordhist[word] = 1
            words = set(self.matchalist.findall(title))
            if words:
                for word in words:
                    if word in self.wordhist:
                        self.wordhist[word] += 1
                    else:
                        self.wordhist[word] = 1

        stwordhist = sorted( self.wordhist.items(), key = lambda x:-x[1] )
        return stwordhist
    


