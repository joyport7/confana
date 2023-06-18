#!/usr/bin/env python
# coding: utf-8

import re

class parseTitle:
    def __init__(self,titles):
        self.seplist = re.compile(":\s|-based|(?:\s|^)(?:a|an|the|in|based on|on|to|of|with|without|by|from|for|via|toward|towards|beyond|using|and|or|as|is|am|are)(?:\s|$)",re.IGNORECASE)
        self.replist = re.compile("^\s|^(?:a|an|the|in)\s|\s(?:a|an|the|in)\s|[^si](s)$|^\s$|^in$",re.IGNORECASE)
        self.pulist = re.compile("(3d reconstruction|object detection|object recognition|object categorization|6d pose|face recognition|face detection|face verification|face identification|\
pedestrian detection|open dataset|knowledge distillation|style transfer|character recognition|character region detection|text spot|\
semantic segmentation|instance segmentation|image segmenation|object tracking|image retrieval|metric learning|pre training|fine tuning|fully convolutional network|Neural Radience Field|Light field|\
action recognition|re identification|image classification|deformable matching|deformable object|non　rigid|weak supervision|transformer|autoencoder|decoder|\
knowledge transfer|domain adapation|domain adaptation|reinforcement learning|transfer learning|active learning|multi modal|cross modal|\
simultaneous localization and mapping|federated learning|point cloud|Siamese|wild|disentangl|E2E|end to end|sparse|adversarial|weakly supervised|\
weak supervision|self supervis|one shot|few shot|zero shot|image generation|video generation|question answer|captioning|\
diffusion|human computer interaction|attention|representation learning|contrastive learning|continual learning|incremental learning|\
unsupervised|semi supervised|noisy label|soft label|deep neural network|boosting|boost|expert|spatio temporal|\
multi task learning|multiple instance learning|multi instance learning|Kullback Leibler)s*",re.IGNORECASE)
        self.malist = re.compile("[^\s-](SLAM|CNN|R CNN|RCNN|RNN|LSTM|CTC|SOM|GAN|ICA|PCA|U NET|UNET|Nerf|SVM|Bagging|MOE|\
Random forest|RF|KL divergence|DNN|GBM)s*[-\s$]")
        self.plist = re.compile(".+?\s(?:interaction|estimation|prediction|alignment|detection|recognition|classification|segmentation|\
identification|retrieval|generation|prediction|inpainting|labeling|distillation|visualizaton|reconstruction|enhancement|\
editing|idenfication|verification|authentication|restoration|tracking|matching|categorization|denoising|navigation|Attack|Grounding|amplification|Captioning|\
answering|answer|Recovery|Parsing|localization|retargeting|relocalization|Synthesis|Correction|Searching|search|compression|Rendering|DeepFake|Reading|\
benchmark|benchmarking|animation|Translation)s*",re.IGNORECASE)
        self.mlist = re.compile("\w+[-\s]*(?:clustering|graph|training|transfer|Defocus|Regression|supression|synthetic|resolution|adaptation|network|\
fusion|reasoning|topology|space|modeling|model|learning|Feature|Generalization|Detector|\
classifier|recognizer|minimization|maxmization|Expression|label|Descriptor|extractor|sparcification|regularization|quantization|coarse to fine)s*|\
Independent Component",re.IGNORECASE)
        #llist = re.compile("",re.IGNORECASE)
        self.tlist = re.compile(".*(?:3D|rgbd|video|frame|dataset|camera|infrared|depth|lider|3D|Text to Image|imagenet|wordnet)[-s]*",re.IGNORECASE)
        self.titles = titles
        self.wordhist = {}

    def wordfreq(self):
        for title in self.titles:
            #print(title)
            sepwords = self.seplist.split(title)
            bMatch = 0
            for item in sepwords:
                item = self.replist.sub("", item)
                item = re.sub( r'-' , " ", item )
                #####
                words = self.pulist.findall(item)
                if words:
                    for word in words:
                        if word in self.wordhist:
                            self.wordhist[word] += 1
                        else:
                            self.wordhist[word] = 1
                words = self.malist.findall(item)
                if words:
                    for word in words:
                        if word in self.wordhist:
                            self.wordhist[word] += 1
                        else:
                            self.wordhist[word] = 1
                words = self.plist.findall(item)
                if words:
                    for word in words:
                        if word in self.wordhist:
                            self.wordhist[word] += 1
                        else:
                            self.wordhist[word] = 1
                words = self.mlist.findall(item)
                if words:
                    for word in words:
                        if word in self.wordhist:
                            self.wordhist[word] += 1
                        else:
                            self.wordhist[word] = 1
                words = self.tlist.findall(item)
                if words:
                    for word in words:
                        if word in self.wordhist:
                            self.wordhist[word] += 1
                        else:
                            self.wordhist[word] = 1

        stwordhist = sorted( self.wordhist.items(), key = lambda x:-x[1] )
        return stwordhist
    


