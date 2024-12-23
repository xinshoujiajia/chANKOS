### 11.7  通用性的含义

当我们首次在第3章中讨论元胞自动机、图灵机、替换系统、寄存器机器等时，每种系统都显得相当不同。但早在第3章中，我们就发现，在整体行为层面上，它们都具有某些共同特征。而现在，最终，通过从计算的角度进行思考，我们可以开始理解为什么会出现这种情况。

正如前两节[5,6]所示，主要观点是，尽管这些不同类型的系统在底层结构上存在巨大差异，但本质上它们最终都可以相互模拟。

这是一个非常显著的结果，也是我在本书中发展的新型科学的关键所在。

从某种意义上说，它最重要的后果是，从计算的角度来看，具有非常不同底层结构的各种系统在某种程度上从根本上来说是等价的。因为人们可能会认为，我们在第3章中讨论的每一种不同类型的系统都能够执行完全不同类型的计算。

但我们在这里发现的情况并非如此。相反，事实证明，基本上每一种系统最终都能够执行完全相同类型的计算。

除此之外，这意味着纯粹从抽象的角度讨论计算的概念确实是有意义的，而无需涉及任何特定类型的系统。因为我们现在知道，最终我们使用的系统类型并不重要：在本质上，任何类型的系统都可以被编程来执行相同的计算。因此，如果我们从抽象层面研究计算，我们可以期望得到的结果将适用于非常广泛的实际系统。

但应该强调的是，在任何特定类型的系统（比如元胞自动机）中，并非所有可能的底层规则都能支持相同类型的计算。

事实上，正如我们在本章开头所看到的，一些元胞自动机只能执行非常简单的计算，例如总是产生纯粹的重复模式。但关键点是，当我们观察计算能力逐渐增强的元胞自动机时，最终会跨越通用性的门槛。一旦跨越这个门槛，能够执行的计算集将始终完全相同。

(p 674)

人们可能会认为，通过使用越来越复杂的底层规则，总是能够构建出计算能力越来越强的系统。但通用性现象表明，情况并非如此，一旦跨越了通用性的门槛，从某种意义上说，就无法再获得更多。

事实上，一旦我们拥有一个通用的系统，其属性就与其构建的细节惊人地无关。就系统能够执行的计算而言，无论系统的底层规则多么复杂，甚至无论系统是元胞自动机、图灵机还是其他什么，都无关紧要。我们将看到，这一相当显著的事实构成了解释我们在第3章中观察到的许多现象的基础，也构成了发展本书中新型科学所需的大部分概念框架的基础。

