### 8.1  建模问题

在上一章中，我展示了如何通过简单的程序思维来理解自然界中常见的各种一般行为模式。在本章中，我将利用所学知识，审视一系列特定类型的自然系统以及其他系统中的行为，并讨论它们最明显行为特征的产生方式。

我所考虑的大多数系统都来自日常生活，初看起来，人们可能会认为这些行为起源早已被揭示。但事实上，在几乎所有情况下，我们对这些系统的了解都相当有限，而且这些行为在根本上往往曾显得相当神秘。但本章我们将发现，通过简单的程序思维，这些行为的基本起源将变得不那么神秘。

需要说明的是，我并非旨在解释我所讨论的各类系统的每一个细节。事实上，即使只是针对某一类系统，要做到这一点也很可能需要另一本甚至多本书籍的篇幅。

但我的目标是识别出导致每类系统行为最明显特征的基本机制。例如，我希望理解雪花为何会形成如此复杂的形状。但我并不关注诸如雪花尖端的确切曲率等细节。

(p 363)

在大多数情况下，我采取的基本方法是尝试为每个系统构建尽可能简单的模型。从传统科学的直觉出发，我们可能会认为如果系统的行为复杂，那么该系统的任何模型也必须在某种程度上同样复杂。

但本书的一个核心发现是，事实并非如此。至少，如果从程序而不是传统数学方程的角度来思考，那么即使基于极其简单的基本规则构建的模型，也能产生极为复杂的行为。事实上，在本章中，我将构建一系列非常简单的模型，这些模型在再现广泛日常自然系统和其他系统中复杂行为的主要特征方面表现相当出色。

任何模型最终都是对系统某些方面的理想化描述，而其他方面则被忽略。当然，在我所考虑的每种系统中，都有许多细节是我所讨论的模型没有涉及的。但在大多数情况下，过去从未有过能够再现我们所见行为最明显特征的模型。因此，我所讨论的模型能够产生大致正确的图像，这本身就是重大的进步。

在许多传统科学领域，任何能够产生此类图像的模型都会立即被视为高度成功。但在一些领域——尤其是那些传统数学应用最广泛的领域——人们开始相信，从某种意义上说，检验模型的唯一真正客观或科学的方法是观察某些相当具体的细节。

最常见的做法是从系统的观测行为中提取出一小组数字，然后观察这些数字能否被模型准确地再现。对于整体行为相对简单的系统，这种方法确实经常非常有效。但当整体行为复杂时，仅通过几个数字就无法完全描述其特征。

(p 364)

事实上，在传统科学的文献中，我经常看到一些模型被认真对待，因为它们能够再现几个特定的数字，但如果人们计算出它们所暗示的整体行为，就会发现这些模型完全是错误的。根据我的经验，评估模型的第一步，远非查看数字或其他细节，而是要用眼睛观察，并将系统的整体图像与模型中的图像进行比较。

如果几乎没有相似之处，那么可以合理地得出结论，该模型是错误的。但如果存在一些相似之处和一些差异，那么就必须判断这些差异是否至关重要。这往往至少部分取决于人们打算如何使用该模型。但凭借适当的判断，从观察整体行为中，通常不难至少对某个模型是否走在正确的道路上有所感觉。

通常，如果模型的复杂程度几乎与被其描述的现象一样复杂，那么这并不是一个好兆头。而更糟糕的是，当进行新的观测时，模型需要不断打补丁以解释这些观测结果。

另一方面，如果一个模型既简单又能大致再现某个系统的许多特征，这通常是一个好兆头。而如果这些特征中有相当一部分是在模型最初构建时未知或至少没有明确考虑的，那么这更是一个好兆头。

人们可能会认为，最终总是可以通过明确观察系统中足够低级的底层元素，并将其与模型中的元素进行比较，来判断模型是否正确。但人们必须意识到，模型只是为系统提供一个抽象的表示——并不能说明该表示中的各个元素必须与系统本身的元素有直接对应关系。

例如，传统的数学模型可能会说，行星的运动由一组微分方程控制。但人们不会认为这意味着行星本身包含一个明确求解这些方程的装置。相反，这些方程提供了一种抽象表示，用于描述实际决定行星运动的物理效应。

(p 365)

当我就本章中的模型与其他科学家进行讨论时，我经常会遇到关于这些问题的巨大困惑。也许这是因为在一个简单的程序中，很容易看到底层元素和控制它们的规则。但无数次有人问我，基于简单程序的模型怎么可能正确，因为即使它们可能成功地再现了某些系统的行为，但人们可以清楚地看到，系统本身并不真正由例如遵循元胞自动机规则的离散单元组成。

但关键在于，任何模型——无论是元胞自动机、微分方程还是其他任何东西——都应该提供对决定系统行为的重要效应的抽象表示。在这些效应之下，模型没有必要像系统本身那样运作。

例如，可以很容易地设置一个元胞自动机来表示在雪花表面新添加的物质点上抑制生长的效果。但在元胞自动机中，这种效果只是通过某些细胞配置的规则来实现的——并且没有必要使这些规则与水分子的详细动力学有任何对应关系。

因此，尽管系统和模型中的元素之间不需要有任何对应关系，但人们可能会认为效应之间必须存在某种完全的对应关系。但模型的意义在于提供一个系统的简化表示，从中可以很容易地推断或理解人们感兴趣的特征。而实现这一点的唯一方法是挑选出某些重要的效应，并忽略所有其他效应。

实际上，在实践中，构建模型的主要挑战正是要确定哪些效应足够重要以至于必须保留，哪些则不然。在一些简单的情况下，有时可以设置实验，基本上可以隔离每个单独的效应并明确测量其重要性。但在大多数情况下，证明某一特定效应集实际上是最重要的最佳证据最终只来自于基于这些效应构建的模型的成功。

(p 366)

本章中我讨论的系统大多足够复杂，至少有数十种截然不同的效应可能对其整体行为产生贡献。但在尝试构建尽可能简单的模型时，我总是挑选出我认为最重要的几个效应。不可避免地，会有一些现象依赖于其他效应，因此我考虑的模型无法正确再现这些现象。因此，如果这些现象对于某些特定应用至关重要，那么别无选择，只能为该应用扩展模型。

但只要在目标是为了理解导致整体行为最明显特征的基本机制方面，保持基础模型尽可能简单就非常重要。因为即使只有几个扩展，模型通常也会变得非常复杂，以至于几乎无法判断任何特定行为特征的真实来源。

多年来，我能够观察到也许有十几个重要模型的进展，这些模型是我为各种具有复杂行为的系统构建的——尽管在大多数情况下从未发表过。我的原始模型通常极其简单。而人们对它们的初步反应通常是惊讶于如此简单的模型竟然能产生具有大致正确特征的行为。但涉及特定类型系统的专家通常会很快指出，我的模型没有正确再现许多细节。

然后，在模型经常被认为过于简单而不值得考虑的初期之后，开始有各种扩展被添加进来，以尝试捕捉更多的效应和细节。结果是，几年后，我的原始模型已经演变成几乎无法辨认的复杂模型。但这些模型随后经常被成功地用于许多实际目的。而在这一点上，随着它们的成功确立，有时会仔细检查这些模型——然后发现许多添加的扩展实际上是不必要的，因此最终，也许十年后，人们会认识到与我最初提出的简单模型等效的模型确实工作得很好。

(p 367)

人们可能会认为，在传统科学的文献中，会不断提出新的模型。但事实上，在几乎每个科学领域所做的工作的绝大多数都不是开发新模型，而是积累实验数据或研究现有模型的后果。

在已经使用的模型中，几乎所有超越纯粹描述性水平的模型最终都以非常相似的方式制定出来：通常是作为数学方程式的集合。但正如我在本书开头所强调的，我认为这是过去很难找到行为复杂的系统可行模型的主要原因。而本书的中心思想之一就是超越数学方程，考虑基于程序的模型，这些程序可以有效地包含任何类型的规则。

在许多方面，与方程相比，与程序一起工作更容易。因为一旦有了程序，就可以通过运行它来找出它的行为将是什么。然而，对于方程，可能需要进行复杂的数学分析才能找出它能导致什么行为。基于方程的模型通常以纯粹隐式的形式表述，这无助于问题的解决，因为它们并没有像程序那样给出确定系统如何行为的实际程序，而只是给出了行为必须满足的约束，并且没有提供关于找出如果有的话，什么行为将实际满足这些约束的特别指导。

即使基于方程的模型可以以显式形式编写，它们通常也涉及连续变量，这些变量例如不能由实用计算机直接处理。当它们的整体行为足够简单时，有时可以找到描述这种行为的完整数学公式。但一旦行为变得更复杂，通常别无选择，只能使用某种形式的近似。尽管过去五十年左右进行了许多尝试，但几乎从未能够证明从这些近似中获得的结果甚至正确地再现了原始数学方程所隐含的内容。

(p 368)

然而，基于简单程序的模型则不会遇到这样的问题。因为从本质上讲，这些模型只涉及可以在实际计算机上直接处理的离散元素。这意味着原则上，计算出这些模型的基本结果变得直接明了，而且在实际操作中往往效率极高。

本章中我所讨论的许多模型，实际上都是基于本书中我所考虑的最简单的程序类型之一。但正如我们将看到的那样，即使这些模型也足以捕捉来自自然界和其他地方的极其广泛的系统的行为——我坚信，这无可置疑地证明了以简单程序为思考方式的实用价值。



