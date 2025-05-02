#!/usr/bin/env python
# coding: utf-8

import re

class parseTitle:
    def __init__(self,titles):
        self.seplist = re.compile(":\s|-based|(?:\s|^)(?:a|an|the|in|based on|on|to|of|with|without|by|from|for|via|toward|towards|beyond|using|and|or|as|is|am|are)(?:\s|$)",re.IGNORECASE)
        self.replist = re.compile("^\s|^(?:a|an|the|in)\s|\s(?:a|an|the|in)\s|[^si](s)$|^\s$|^in$",re.IGNORECASE)
        
        self.plist = "interact|estimat|predict|align|detect|recogni|classifi|segment|memor|recommend|cluster|transfer|defocus|regress|supression|synthe|adapt|fusion|reasoning|\
identifi|retriev|evaluat|generat|predict|inpaint|distill|visualizaton|reconstruct|enhance|generaliz|represent|minimiz|maxmiz|label|descript|extract|regulariz|quantiz|\
edit|verif|authenticat|restor|track|match|categoriz|denois|navigat|attack|grounding|amplifi|caption|answer|recover|parsing|localiz|retarget|relocaliz|correction|search|compress|render|read|\
benchmark|animation|translat|fairness|responsible|trustworth|prun|question answer|manipulat|locomotion|tokeniz|safe|imbalance|unbalance|mining|interpret|\
consisten|guarantee|encod|decod|discover|modulat|inductive bias|massive|bias|mosaic|physical world|\
collaborat|reliable|Multi hop|multi turn|Multi step|diagnosis|decision making|temporal abstraction|scalabl|asynchron|rare|in the wild|\
episod|calibration|data analysis|jailbreak|stationary|composition|structur|watermark|gesture|data association|domain generaliz|domain randomiz|\
boundary|poison|overfit|explanation|super resolution|prompt|rerank|ranking|symbol|embod|OCR|character recognition|assembly|\
next token prediction|system identification|entropy minimiz|maximum entropy|tool calling|function calling|backdoor|attack|sensor|annotat|vehicle|toxic|deep\s*fake|\
multilingual|moderation|budget|constrain|salien|interven|llm as a judge|out of distribution|OOD|outlier|iid|horizon|panoptic segmentation|\
diagram analysis"
        self.pulist = "3D reconstruction|scene reconstruction|object detec|object recogni|object categoriz|6d pose|pose estimat|face recogni|face detect|face verifi|face identifi|\
pedestrian detection|open dataset|open set|knowledge distillation|style transfer|character recogni|character region detection|text spot|facial expression|\
semantic segmentation|instance segmentation|image segmenation|object tracking|metric learning|pre\s*train|fine tun|preference|fully convolutional network|Neural Radience Field|Light field|\
action recognition|re identification|image classifi|deformable matching|deformable object|non rigid|weak supervision|transformer|auto\s*encoder|decoder|\
knowledge transfer|domain adapation|domain adaptation|reinforcement learning|transfer learning|active learning|policy learning|multi\s*modal|cross modal|\
simultaneous localization and mapping|federated learning|point cloud|Siamese|wild|disentangl|end to end|spars|adversarial|weakly supervised|\
weak supervision|self supervis|one shot|few shot|zero shot|image generation|video generation|code generation|speech generation|captioning|Differential privacy|\
diffusion|human computer interaction|attention|representation learning|contrastive learning|continual learning|incremental learning|meta learning|meta RL|\
unsupervised|semi supervised|noisy label|soft label|deep neural network|boosting|boost|expert|spatio\s*temporal|Bayes|Bandit|Combinatorial|\
multi task learning|multi objective|multiple instance learning|multi instance learning|Kullback Leibler|generative|Language Model|tuning|embedding|\
Curriculum|certification|equivariant|(?:normaliz(?:ing|ed) flow)|world model|flow network|multi agent|multi session|long context|feature selection|model selection|data selection|subset selection|\
latent|quantum|low rank|instruction|label|submodular|vision and language|vision lanugage|visual language|speech language|\
in\s*context learning|feedback|demonstration|imitation|forget|unlearn|efficien|feature aggregation|co training|\
perceptual|non\s*convex|convex|activation|context|image text|test time|agent|skill learning|mutual information|workflow|scaling law|lifelong|motion planning|task planning|\
text and image|autonomous|decentraliz|anomaly detection|animation|belief propagation|label propagation"
        self.mlist = "graph|topolog|diffrential|feature|coarse to fine|contrastive|correlation|independent component|importance sampling|k means|nonparametric|parametric|data augment|conditional|\
dynamics|kinematics|counterfactual|manifold|kinetic|perspecitve transform|affine transform|group|branch and bound|rule based|\
augmented reality|mean field|weight decay|grassmann|geodesic|auto regressive|min max|second order|relaxation|\
optimal transport|replay|rehersal|roll\s*out|stochastic|probabilistic|statistical|deterministic|hierarch|prior|posterior|causal|power law|free energy|\
linear|non\s*linear|quadratic|reward|optimal control|control system|bootstrap|curios|intrinsic|retrieval augmented|perturbat|randomize|long short term|spiking|\
exploration or exploitation|associative memor|factual|student|Chi-Squar|nearest neighbour|sliding window|advantage function|behavioral cloning|subspace|\
state space model|hidden Markov model|gaussian mixture|cross validation|joint probability|black box|genetic|residual|ensembl|dynamic programming|bag of words|\
information theoretic|chain of thought|codebook|word2vec|covariance|dictionary|online|offline|policy optimization|value based|off policy|on policy|policy gradient|homogeneous|Heterogeneous"
        self.tlist = "graphics|game|rgbd|video|dataset|camera|infrared|depth|lider|Text to Image|imagenet|wordnet|image|sound|speech|gene\s|finance|time series|music|acoustic|siganl|\
geometry|robot|molecule|token|fluid|simulation|cyber physical|digital twin|radar|lidar|weather|fingerprint|drug|material|missile|color|phase|frequency|cell|\
physics|chemic|medic|brain|quantum|atomic|radio freqency|surgi|protein|genome|tactile|haptic|meal|cook|ASR|humanoid|document|slide|poster|advertiz|KV Cache|mode collapse|\
articulated|lasso|ridge|mixture of expert|foundation model|mamba|generative model|Markov decision process|Markov chain Monte carlo|Partialy* observabl|Random forest|\
Actor critic|latent diffusion|predictive control|Bayesian flow|flow matching|Gaussian splat|gaussian process|adam|singular"
        self.malist = "RL|L\s*1|L\s*0|CAD|3D|DNA|RNA|EEG|EMG|EM|ODE|BRDF|SLAM|CNN|R CNN|RCNN|DNN|SNN|RNN|LSTM|CTC|SOM|GAN|ICA|PCA|CRF|MRF|MCMC|LDA|U NET|UNET|Nerf|SVM|SVD|eigen|Bagging|MOE|ODE|PDE|LLM|SLM|LVLM|VLM|MM LLM|E2E|\
SDF|DAG|XAI|ELSI|MDP|POMDP|RLHF|RF|KL divergence|DNN|GBM|VAE|ODE|PDE|CLIP|PPO|DPO|DQN|DDPG|TRPO|SAC|A3C|UNREAL|R2D2|SARSA|segment anything|LoRA|YOLO|GP|GMM|SE\(3\)|SO\(3\)|\
RAG|CEM|LDM|SAM|MPC|KF|EKF|SGD|Monte Calro|Lipschitz|\
Bellman|Kalman|Jensen|Shannon|Neumann|Euler|Newton|Dirichlet|Rieman|kernel|Hilbert|Wasserstein|Bregman|Langevin|Fisher|Kolmogorov|Voronoi|Bhattacharyya|Bernoulli|Nash|Markov|Liyapunov|Hessian|Jacobian|Hamilton|Lagrange|Hadamard"

        self.matchlist = re.compile(self.plist+"|"+self.pulist+"|"+self.mlist+"|"+self.tlist,re.IGNORECASE)
        self.matchalist = re.compile(self.malist)

        self.titles = titles
        self.wordhist = {}

    def wordfreq(self):
        for title in self.titles:
            try:
                title = title.lower()
            except:
                print(title)
            title = re.sub( r'-' , " ", title )
            title = re.sub( r'&' , "and", title )
            title = re.sub( r'sation' , "zation", title )
            title = re.sub( r'ising' , "izing", title )

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
    


