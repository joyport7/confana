#!/usr/bin/env python
# coding: utf-8

import re

class parseTitle:
    def __init__(self,titles):
        self.seplist = re.compile(":\s|-based|(?:\s|^)(?:a|an|the|in|based on|on|to|of|with|without|by|from|for|via|toward|towards|beyond|using|and|or|as|is|am|are)(?:\s|$)",re.IGNORECASE)
        self.replist = re.compile("^\s|^(?:a|an|the|in)\s|\s(?:a|an|the|in)\s|[^si](s)$|^\s$|^in$",re.IGNORECASE)
        
        #self.plist = "interact|estimat|predict|align|detect|recogni|classifi|segment|memor|recommend|cluster|transfer|defocus|regress|supression|synthe|adapt|fusion|reasoning|identifi|retriev|evaluat|generat|predict|inpaint|distill|visualizaton|reconstruct|enhance|generaliz|represent|minimiz|maxmiz|label|descript|extract|regulariz|quantiz|edit|verif|authenticat|restor|track|match|categoriz|denois|navigat|attack|grounding|amplifi|caption|answer|recover|parsing|localiz|retarget|relocaliz|correction|search|compress|render|read|benchmark|animation|translat|fairness|responsible|trustworth|prun|question answer|manipulat|locomotion|tokeniz|safe|imbalance|unbalance|mining|interpret|consisten|guarantee|encod|decod|discover|modulat|inductive bias|massive|bias|mosaic|physical world|collaborat|reliable|Multi hop|multi turn|Multi step|diagnosis|decision making|temporal abstraction|scalab|asynchron|rare|in the wild|episod|calibration|data analysis|jailbreak|stationary|composition|structur|watermark|gesture|data association|domain generaliz|domain randomiz|boundary|poison|overfit|explanation|super resolution|prompt|rerank|ranking|symbol|embod|OCR|character recognition|assembly|next token prediction|system identification|entropy minimiz|maximum entropy|tool calling|function calling|backdoor|attack|sensor|annotat|vehicle|toxic|deep\s*fake|multilingual|moderation|budget|constrain|salien|interven|llm as a judge|out of distribution|ood|outlier|iid|horizon|panoptic segmentation|diagram analysis"
        #self.pulist = "3D reconstruction|scene reconstruction|object detec|object recogni|object categoriz|6d pose|pose estimat|face recogni|face detect|face verifi|face identifi|pedestrian detection|open dataset|open set|knowledge distillat|style transfer|character recogni|character region detect|text spot|facial expression|semantic segmentation|instance segmentation|image segmenation|object tracking|metric learning|pre\s*train|fine tun|preference|fully convolutional network|Neural Radience Field|Light field|action recognition|re identification|image classifi|deformab matching|deformable object|non rigid|weak supervision|transformer|auto\s*encoder|decoder|knowledge transfer|domain adapation|domain adaptation|reinforcement learning|transfer learning|active learning|policy learning|multi\s*modal|cross modal|simultaneous localization and mapping|federated learning|point cloud|Siamese|wild|disentangl|end to end|spars|adversarial|weakly supervised|weak supervision|self supervis|one shot|few shot|zero shot|image generation|video generation|code generation|speech generation|captioning|Differential privacy|diffus|human computer interaction|attention|representation learning|contrastive learning|continual learning|incremental learning|meta learning|meta RL|unsupervised|semi supervised|noisy label|soft label|deep neural network|boosting|boost|expert|spatio\s*temporal|Bayes|Bandit|Combinatorial|multi task learning|multi objective|multiple instance learning|multi instance learning|Kullback Leibler|generative|Language Model|tuning|embedding|Curriculum|certification|equivarian|(?:normaliz(?:ing|ed) flow)|world model|flow network|multi agent|multi session|long context|feature selection|model selection|data selection|subset selection|latent|quantum|low rank|instruction|submodular|vision and language|vision lanugage|visual language|speech language|in\s*context learning|feedback|demonstration|imitation|forget|unlearn|efficien|feature aggregation|co training|perceptual|non\s*convex|convex|activation|context|image text|test time|agent|skill learning|mutual information|workflow|scaling law|lifelong|motion planning|task planning|text and image|autonomous|decentraliz|anomaly detection|animation|belief propagation|label propagation"
        #self.mlist = "graph|topolog|diffrential|feature|coarse to fine|contrastive|correlation|independent component|importance sampling|k means|nonparametric|parametric|data augment|conditional|dynamics|kinematics|counterfactual|manifold|kinetic|perspecitve transform|affine transform|group|branch and bound|rule based|augmented reality|mean field|weight decay|grassmann|geodesic|auto regressive|min max|second order|relaxation|optimal transport|replay|rehersal|roll\s*out|stochastic|probabilistic|statistical|deterministic|hierarch|prior|posterior|causal|power law|free energy|linear|non\s*linear|quadratic|reward|optimal control|control system|bootstrap|curios|intrinsic|retrieval augmented|perturbat|randomize|long short term|spiking|exploration or exploitation|associative memor|factual|student|Chi-Squar|nearest neighbour|sliding window|advantage function|behavioral cloning|subspace|state space model|hidden Markov model|gaussian mixture|cross validation|joint probability|black box|genetic|residual|ensembl|dynamic programming|bag of words|information theoretic|chain of thought|codebook|word2vec|covarian|dictionary|online|off\s*line|policy optimization|value based|off policy|on policy|policy gradient|homogeneous|Heterogeneous"
        #self.tlist = "graphics|game|rgbd|video|dataset|camera|infrared|depth|lider|Text to Image|imagenet|wordnet|image|sound|speech|gene\s|finance|time series|music|acoustic|siganl|geometry|robot|molecule|token|fluid|simulation|cyber physical|digital twin|radar|lidar|weather|fingerprint|drug|material|missile|color|phase|frequency|cell|physics|chemic|medic|brain|quantum|atomic|radio freqency|surgi|protein|genome|tactile|haptic|meal|cook|ASR|humanoid|document|slide|poster|advertiz|KV Cache|mode collapse|articulated|lasso|ridge|mixture of expert|foundation model|mamba|generative model|Markov decision process|Markov chain Monte carlo|partial(?:ly) observab|Random forest|Actor critic|predictive control|Bayesian flow|flow matching|Gaussian splat|gaussian process|adam|singular"
        #self.malist = "OOD|RL|L\s*1|L\s*0|CAD|3D|DNA|RNA|EEG|EMG|EM|ODE|BRDF|SLAM|CNN|R CNN|RCNN|DNN|SNN|RNN|LSTM|CTC|SOM|GAN|ICA|PCA|CRF|MRF|MCMC|LDA|U NET|UNET|Nerf|SVM|SVD|eigen|Bagging|MOE|ODE|PDE|LLM|SLM|LVLM|VLM|MM LLM|E2E|SDF|DAG|XAI|ELSI|MDP|POMDP|RLHF|RF|KL divergence|DNN|GBM|VAE|ODE|PDE|CLIP|PPO|DPO|DQN|DDPG|TRPO|SAC|A3C|UNREAL|R2D2|SARSA|segment anything|LoRA|YOLO|GP|GMM|SE\(3\)|SO\(3\)|RAG|CEM|LDM|SAM|MPC|KF|EKF|SGD|Monte Calro|Lipschitz|Bellman|Kalman|Jensen|Shannon|Neumann|Euler|Newton|Dirichlet|Rieman|kernel|Hilbert|Wasserstein|Bregman|Langevin|Fisher|Kolmogorov|Voronoi|Bhattacharyya|Bernoulli|Nash|Markov|Liyapunov|Hessian|Jacobian|Hamilton|Lagrange|Hadamard"

        #self.matchlist = re.compile(self.plist+"|"+self.pulist+"|"+self.mlist+"|"+self.tlist,re.IGNORECASE)
        #self.matchalist = re.compile(self.malist)

        self.matchlist = ['(normaliz.+? flow)','(3D reconstruction)','(6d pose)','(acoustic)','(action recognition)','(activation)','(active learning)','(Actor critic)','(adam)','(adapt)[a-z]*?','(advantage function)','(adversarial)','(advertiz)[a-z]+?','(affine transform)[a-z]+?','(agent)[a-z]+?','(align)[a-z]+?','(amplifi)[a-z]+?','(animat)[a-z]+?','(annotat)[a-z]+?','(anomaly detection)','(answer)[a-z]*?','(articulat)[a-z]+?','(assembly)','(associative memor)','(asynchron)[a-z]+?','(atomic)','(attack)','(attent)[a-z]+?','(augmented reality)','(authenticat)[a-z]+?','(auto regress)[a-z]+?','(auto\s*encoder)','(autonomous)','(backdoor)[s]*','(bag of words)','(Bandit)[s]*','(Bayes)[a-z]+?','(Bayesian flow)','(behavioral cloning)','(belief propagation)','(benchmark)[a-z]*?','(bias[a-z]+?)','(black box)','(boost)[a-z]*?','(bootstrap)[a-z]*?','(boundary)','(brain)','(branch and bound)','(budget)[s]*','(calibrat)[a-z]+?','(camera)[s]*','(caption)[a-z]*?','(categoriz)[a-z]+?','(causal)[a-z]+?','(cell)[s]*','(certification)','(chain of thought)','(character recogni)[a-z]+?','(character region detect)[a-z]+?','(chemic)[a-z]+?','(Chi-Square)[s]*','(classifi)[a-z]+?','(cluster)[s]*','(co train)[a-z]+?','(coarse to fine)','(code generation)','(codebook)[s]*','(collaborat)[a-z]+?','(color)[a-z]*?','(combinatorial)','(composition)[a-z]*?','(compress)[a-z]*?','(condition)[a-z]*?','(consistent)','(constrain)[a-z]*?','(context)[a-z]*?','(continual learning)','(contrastive)','(control system)[s]*','(convex)','(cook)[a-z]*?','(correct)[a-z]*?','(correlat)[a-z]+?','(counterfactual)','(covarian)[a-z]+?','(cross modal)[a-z]*?','(cross validat)[a-z]+?','(curios)[a-z]*?','(curriculum)[s]*','(cyber physical)','(data analysis)','(data association)','(data augment)[a-z]+?','(data selection)','(dataset)','(decentraliz)[a-z]+?','(decision making)','(decod)[a-z]+?','(deep neural network)[s]*','(deep\s*fake)','(defocus)','(deform)[a-z]+?','(demonstrat)[a-z]+?','(denois)[a-z]+?','(depth)','(descript)[a-z]+?','(detect)[a-z]*?','(deterministic)','(diagnosis)[a-z]+?','(diagram analysis)','(dictionar)[a-z]+?','(differential privacy)','(diffus)[a-z]+?','(digital twin)[s]*','(discover)[a-z]*?','(disentangl)[a-z]+?','(distill)[a-z]*?','(document)[s]*','(domain adaptation)','(domain generalization)','(domain randomization)','(drug)[s]*','(dynamic programming)','(dynamics)','(edit)[a-z]*?','(efficien)[a-z]+?','(embed)[a-z]+?','(embod)[a-z]+?','(encod)[a-z]+?','(end to end)','(enhance)[a-z]+?','(ensembl)[a-z]+?','(entropy minimization)','(episode)[s]*','(equivariant)','(estimat)[a-z]+?','(evaluat)[a-z]+?','(expert)[s]*','(expla)[a-z]+?','(exploration or exploitation)','(extract)[a-z]*?','(face detect)[a-z]+?','(face identifi)[a-z]+?','(face recogni)[a-z]+?','(face verifi)[a-z]+?','(face expression)','(facial detect)[a-z]+?','(facial identifi)[a-z]+?','(facial recogni)[a-z]+?','(facial verifi)[a-z]+?','(facial expression)','(factual)[a-z]*?','(fair)[a-z]+?','(feature)[s]*','(feature aggregat)[a-z]+?','(feature select)[a-z]+?','(federat)[a-z]+?','(feedback)[s]*','(few shot)[s]*','(financ)[a-z]+?','(fine tun)[a-z]+?','(fingerprint)[a-z]*?','(flow match)[a-z]*?','(flow network)[s]*','(fluid)','(forget)[a-z]*?','(foundation model)[s]*','(free energy)','(frequency)','(fully convolutional network)[s]*','(function call)[a-z]*?','(fusion)','(game)[s]*','(gaussian mixture)','(gaussian process)','(Gaussian splat)[a-z]+?','(gene)[s]*','(generaliz)[a-z]+?','(generat)[a-z]+?','(generative model)','(genetic)','(genome)[s]*','(geodesic)','(geometry)','(gesture)[s]*','(graph)[s]*','(graphics)[s]*','(grassmann)[a-z]*?','(ground)[a-z]+?','(group)[a-z]*?','(guarantee)','(haptic)','(heterogeneous)','(hidden Markov model)[s]*','(hierarch)[a-z]+?','(homogeneous)','(horizon)','(human computer interaction)','(humanoid)s*','(identifi)[a-z]+?','(iid)','(i\.i\.d\.)','(image)','(image classifi)[a-z]+?','(image generat)[a-z]+?','(image segment)[a-z]+?','(image text)[s]*','(imagenet)[s]*','(imbalance)[a-z]*?','(imitat)[a-z]+?','(importance sampling)','(in the wild)','(in\s*context learning)','(incremental learning)','(independent component)','(inductive bias)','(information theor)[a-z]*?','(infra-*red)','(inpaint)[a-z]+?','(instance segmentation)','(instruction)','(interact)[a-z]+?','(interpret)[a-z]+?','(interven)[a-z]+?','(intrinsic)','(jailbreak)[a-z]*?','(joint probability)','(k means)','(kinematic)[s]*','(kinetic)','(knowledge distillat)[a-z]+?','(knowledge transfer)[a-z]*?','(Kullback Leibler)','(KV Cache)','(label)[a-z]*?','(label propagation)','(language model)[s]*','(lasso)','(latent)','(lidar)','(lifelong)','(light field)[s]*','(linear)','(llm as a judge)','(localiz)[a-z]+?','(locomotion)','(long context)','(long short term)','(low rank)','(mamba)','(manifold)[s]*','(manipulat)[a-z]+?','(Markov chain Monte carlo)','(Markov decision process)','(massive)','(match)[a-z]*?','(material)','(maximum entropy)','(maxmiz)[a-z]+?','(meal)','(mean field)','(medic)[a-z]+?','(memor)[a-z]+?','(meta learning)','(meta RL)','(metric learning)','(min max)','(minimiz)[a-z]+?','(mining)','(missile)','(mixture of expert)[s]*','(mode collapse)','(model selection)','(moderation)','(modulat)[a-z]+?','(molecule)[s]*','(mosaic)[a-z]*?','(motion plann)[a-z]+?','(multi agent)[s]*','(multi hop)','(multi[a-z]+? instance learning)','(multi[a-z]+? objective)','(multi[a-z]+? session)','(Multi[a-z]+? step)','(multi[a-z]+? task learning)','(multi turn)','(multi\s*modal)','(multilingual)','(music)[s]*','(mutual information)','(navigat)[a-z]+?','(nearest neighbour)[s]*','(Neural Radience Field)[s]*','(next token prediction)','(noisy label)[s]*','(non rigid)','(non\s*convex)','(non\s*linear)','(nonparametric)','(object categor)[a-z]+?','(object detec)[a-z]+?','(object recogni)[a-z]+?','(object tracking)','(off policy)','(off\s*line)','(on policy)','(one shot)','(on\s*line)','(ood)','(open dataset)','(open set)','(optimal control)','(optimal transport)[s]*','(out of distribution)','(outlier)[s]*','(overfit)[a-z]+?','(panoptic segmentation)','(parametric)','(parsing)','(partial(?:ly) observab)','(pedestrian detection)','(perceptual)','(perspecitve transform)[a-z]*?','(perturbat)[a-z]+?','(phase)[s]*','(physical world)[s]*','(physics)','(point cloud)[s]*','(poison)[a-z]*?','(policy gradient)[s]*','(policy learning)','(policy optimiz)[a-z]+?','(pose estimat)[a-z]+?','(poster)[s]*','(posterior)[s]*','(power law)[s]*','(pre\s*train)[a-z]+?','(predict)[a-z]+?','(predictive control)','(preference)[s]*','(prior)[s]*','(probabilistic)','(prompt)[a-z]*?','(protein)[s]*','(prun)[a-z]+?','(quadratic)','(quantiz)[a-z]+?','(quantum)[s]*','(question answer)[a-z]*?','(rader)[s]*','(radio freqency)','(Random forest)[s]*','(randomiz)[a-z]+?','(ranking)','(rare)','(re\s*identification)','(read)','(reason)[a-z]+?','(recogni)[a-z]+?','(recommend)[a-z]*?','(reconstruct)[a-z]*?','(recover)[a-z]*?','(regress)[a-z]*?','(regulariz)[a-z]+?','(rehersal)','(reinforcement learning)','(relax)[a-z]+?','(reliabl)[a-z]+?','(relocaliz)[a-z]+?','(render)[a-z]*?','(replay)[s]*','(represent)[a-z]*?','(representation learning)','(rerank)[a-z]*?','(residual)','(responsible)','(restor)[a-z]+?','(retarget)[a-z]+?','(retriev)[a-z]+?','(retrieval augmented)','(reward)[a-z]*?','(rgbd)','(ridge)','(robot)[a-z]*?','(roll\s*out)','(rule based)','(safe)[a-z]*?','(salien)[a-z]+?','(scalab)[a-z]+?','(scaling law)','(scene reconstruction)','(search)[a-z]*?','(second order)','(segment)[a-z]+?','(self supervis)[a-z]+?','(semantic segmentation)','(semi supervis)[a-z]+?','(sensor)[s]*','(Siamese)','(signal)[s]*','(simulat)[a-z]+?','(simultaneous localization and mapping)','(singular)[a-z]+?','(skill learning)','(sliding window)[s]*','(soft label)[a-z]*?','(sound)[s]*','(spars)[a-z]+?','(spatio\s*temporal)','(speech)[a-z]*?','(speech generat)[a-z]+?','(speech recogniz)[a-z]+?','(speech language)','(spik)[a-z]+?','(state space model)[s]*','(stationary)','(statistic)[a-z]*?','(stochastic)[a-z]*?','(structur)[a-z]+?','(student)[s]*','(style transfer)','(submodular)[a-z]*?','(subset selection)','(subspace)[s]*','(super resolution)','(supression)','(surgi)[a-z]+?','(symbol)[a-z]*?','(synthe)[a-z]+?','(system identif)[a-z]+?','(tactile)','(task plann)[a-z]+?','(temporaly* abstract)[a-z]+?','(test time)','(text and image)','(text spot)[a-z]+?','(Text to Image)','(time series)','(token)[a-z]+?','(tool call)[a-z]*?','(topolog)[a-z]+?','(toxic)[a-z]*?','(track)[a-z]*?','(transfer)[a-z]*?','(transfer learning)','(transformer)s*','(transformation)s*','(translat)[a-z]+?','(trustworth)[a-z]+?','(tuning)','(unbalance)','(unlearn)[a-z]*?','(unsupervised)','(value based)','(vehicle)[s]*','(verif)[a-z]+?','(video)[s]*','(video generat)[a-z]+?','(vision and language)','(vision lanugage)','(visual language)','(visualiz)[a-z]+?','(watermark)[a-z]*?','(weak supervision)','(weakly supervised)','(weather)','(weight decay)','(word2vec)','(wordnet)','(workflow)[s]*','(world model)[s]*','(zero shot)']
        self.matchlist = [s.lower() for s in self.matchlist]
        self.matchalist = ['(3D)[-]*','(A3C)','(ASR)','(Bagging)','(Bellman)','(Bernoulli)','(Bhattacharyya)','(BRDF)[s]*','(Bregman)','(CAD)','(CEM)','(CLIP)','(CNN)[s]*','(CRF)[s]*','(CTC)','(DAG)[s]*','(DDPG)','(Dirichlet)','(DNA)[-]*','(DNN)[-]*','(DPO)','(DQN)[-]*','(E2E)','(EEG)','(eigen)','(EKF)[-]*','(ELSI)','(EM)','(EMG)[-]*','(Euler)','(Fisher)','(GAN)[-]*','(GBM)[-]*','(GMM)[-]*','(GP)[-]*','(Hadamard)','(Hamilton)','(Hessian)','(Hilbert)','(ICA)','(Jacobian)','(Jensen)','(Kalman)','(kernel)','(KF)[-]*','(KL divergence)','(Kolmogorov)','(L\s*0)','(L\s*1)','(Lagrange)','(Langevin)','(LDA)','(LDM)','(Lipschitz)','(Liyapunov)','(LLM)[-]*','(LoRA)','(LSTM)[-]*','(LVLM)','(Markov)','(MCMC)','(MDP)[-]*','(MM LLM)[-]*','(MOE)[-]*','(Monte Calro)','(MPC)','(MRF)[-]*','(Nash)','(Nerf)','(Neumann)','(Newton)','(OCR)','(ODE)[-]*','(OOD)','(PCA)','(PDE)[-]*','(PDE)[-]*','(POMDP)','(PPO)','(R CNN)','(R2D2)','(RAG)','(RCNN)[-]*','(RF)[-]*','(Rieman)','(RL)','(RLHF)[-]*','(RNA)[-]*','(RNN)[-]*','(SAC)','(SAM)','(SARSA)','(SDF)[-]*','(SE\(3\))','(segment anything)','(SGD)[-]*','(Shannon)','(SLAM)','(SLM)[-]*','(SNN)[-]*','(SO\(3\))','(SOM)','(SVD)','(SVM)','(TRPO)','(U NET)','(UNET)','(UNREAL)','(VAE)','(VLM)','(Voronoi)','(Wasserstein)','(XAI)','(YOLO)']
        self.matchalist = [s.lower() for s in self.matchalist]

        self.titles = titles
        self.wordhist = {}

    def wordfreq_bykw(self):
        for title in self.titles:
            
            #print(title)
            title = title.lower()
            title = re.sub( r'-' , "", title )
            title = re.sub( r'&' , " ", title )
            title = re.sub( r'sation' , "zation", title )
            title = re.sub( r'ising' , "izing", title )

            for pat in self.matchlist:
                #print(pat)
                patt = '(?:^|\s|\:)'+pat+'(?:\s|$|\:)'
                mt = re.findall(patt,title)
                if mt:
                    #print('match')
                    if mt[0] in self.wordhist:
                        self.wordhist[mt[0]] += 1
                    else:
                        self.wordhist[mt[0]] = 1
            
            for pat in self.matchalist:
                #patt = '[^\s]('+pat+')[\s\:\-]'
                patt = '(?:^|\s|\:)'+pat+'(?:\s|$|\:)'
                mt = re.findall(patt,title)
                if mt:
                    if mt[0] in self.wordhist:
                        self.wordhist[mt[0]] += 1
                    else:
                        self.wordhist[mt[0]] = 1

            #words = set(self.matchlist.findall(title))
            #if words:
            #    for word in words:
            #        if word in self.wordhist:
            #            self.wordhist[word] += 1
            #        else:
            #            self.wordhist[word] = 1
            #words = set(self.matchalist.findall(title))
            #if words:
            #    for word in words:
            #        if word in self.wordhist:
            #            self.wordhist[word] += 1
            #        else:
            #            self.wordhist[word] = 1

        stwordhist = sorted( self.wordhist.items(), key = lambda x:-x[1] )
        return stwordhist
    

    def wordfreq_byword(self):
        for title in self.titles:
            try:
                title = title.lower()
            except:
                print(title)
            title = re.sub( r'-' , " ", title )
            title = re.sub( r'&' , "and", title )
            title = re.sub( r'sation' , "zation", title )
            title = re.sub( r'ising' , "izing", title )

            ttlwds = re.split(' ',title)

            for ttlwd in ttlwds:
                try:
                    if ttlwd in self.wordhist:
                        self.wordhist[ttlwd] += 1
                    else:
                        self.wordhist[ttlwd] = 1
                except:
                    print(ttlwd)

        stwordhist = sorted( self.wordhist.items(), key = lambda x:-x[1] )
        return stwordhist
    



